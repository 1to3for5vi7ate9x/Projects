import os
from pytubefix import Playlist, YouTube
from tqdm import tqdm

def sanitize_filename(filename):
    """Sanitize file names to be OS-compatible."""
    return "".join(c if c.isalnum() or c in " .-_()" else "_" for c in filename)

def download_playlist(playlist_url, output_base_dir="downloads"):
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    playlist = Playlist(playlist_url)
    playlist_title = sanitize_filename(playlist.title or "Untitled Playlist")
    playlist_dir = os.path.join(output_base_dir, playlist_title)

    if not os.path.exists(playlist_dir):
        os.makedirs(playlist_dir)

    print(f"Downloading playlist: {playlist_title}")

    video_urls = playlist.video_urls
    for video_url in video_urls:
        try:
            yt = YouTube(video_url)
            try:
                video_title = sanitize_filename(yt.title)
            except Exception:
                print(f"Warning: Unable to fetch title for {video_url}. Using fallback title.")
                video_title = f"video_{yt.video_id}"

            print(f"Downloading video: {video_title}")
            # Download video and audio separately and merge them
            video_stream = yt.streams.filter(file_extension="mp4", only_video=True).order_by("resolution").desc().first()
            audio_stream = yt.streams.filter(only_audio=True).order_by("abr").desc().first()

            video_path = video_stream.download(output_path=playlist_dir, filename=f"{video_title}_video.mp4")
            audio_path = audio_stream.download(output_path=playlist_dir, filename=f"{video_title}_audio.mp4")

            # Merge video and audio
            output_path = os.path.join(playlist_dir, f"{video_title}.mp4")
            os.system(f"ffmpeg -i \"{video_path}\" -i \"{audio_path}\" -c:v copy -c:a aac \"{output_path}\" -y")

            # Clean up intermediate files
            os.remove(video_path)
            os.remove(audio_path)

            print(f"Downloaded video: {output_path}")
        except Exception as e:
            print(f"Error downloading {video_url}: {e}")

def download_single_video(video_url, output_base_dir="downloads"):
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    try:
        yt = YouTube(video_url)
        video_title = sanitize_filename(yt.title or f"video_{yt.video_id}")

        print(f"Downloading video: {video_title}")
        # Download video and audio separately and merge them
        video_stream = yt.streams.filter(file_extension="mp4", only_video=True).order_by("resolution").desc().first()
        audio_stream = yt.streams.filter(only_audio=True).order_by("abr").desc().first()

        video_path = video_stream.download(output_path=output_base_dir, filename=f"{video_title}_video.mp4")
        audio_path = audio_stream.download(output_path=output_base_dir, filename=f"{video_title}_audio.mp4")

        # Merge video and audio
        output_path = os.path.join(output_base_dir, f"{video_title}.mp4")
        os.system(f"ffmpeg -i \"{video_path}\" -i \"{audio_path}\" -c:v copy -c:a aac \"{output_path}\" -y")

        # Clean up intermediate files
        os.remove(video_path)
        os.remove(audio_path)

        print(f"Downloaded video: {output_path}")
    except Exception as e:
        print(f"Error downloading video {video_url}: {e}")

if __name__ == "__main__":
    choice = input("Do you want to download a playlist or a single video? (Enter 'playlist' or 'single'): ").strip().lower()
    
    if choice == "playlist":
        playlist_url = input("Enter the YouTube playlist URL: ").strip()
        download_playlist(playlist_url)
    elif choice == "single":
        video_url = input("Enter the YouTube video URL: ").strip()
        download_single_video(video_url)
    else:
        print("Invalid choice. Please enter 'playlist' or 'single'.")

