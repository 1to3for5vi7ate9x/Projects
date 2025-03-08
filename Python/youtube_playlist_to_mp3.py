import os
from pytubefix import Playlist, YouTube
from moviepy.audio.io.AudioFileClip import AudioFileClip

def sanitize_filename(filename):
    """Sanitize file names to be OS-compatible."""
    return "".join(c if c.isalnum() or c in " .-_()" else "_" for c in filename)

def download_playlist_to_mp3(playlist_url, output_dir="initially"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    playlist = Playlist(playlist_url)
    print(f"Downloading playlist: {playlist.title if playlist.title else 'Untitled Playlist'}")
    
    for video_url in playlist.video_urls:
        try:
            yt = YouTube(video_url)
            try:
                video_title = sanitize_filename(yt.title)
            except Exception:
                print(f"Warning: Unable to fetch title for {video_url}. Using fallback title.")
                video_title = f"video_{yt.video_id}"
            
            print(f"Downloading video: {video_title}")
            video_stream = yt.streams.filter(only_audio=True).first()
            video_file = video_stream.download(output_path=output_dir, filename=f"{video_title}.mp4")
            
            mp3_file = os.path.join(output_dir, f"{video_title}.mp3")
            print(f"Converting to MP3: {video_title}")
            with AudioFileClip(video_file) as audio_clip:
                audio_clip.write_audiofile(mp3_file)
            
            os.remove(video_file)
            print(f"Downloaded and converted: {mp3_file}")
        except Exception as e:
            print(f"Error downloading {video_url}: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_playlist_to_mp3(playlist_url)

