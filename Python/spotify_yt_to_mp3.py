import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import youtube_dl

# Spotify credentials
SPOTIFY_CLIENT_ID = "5a60b1d47daf479aa928d62888bd1787"
SPOTIFY_CLIENT_SECRET = "b2d5dc22b238439ab3709a5a2f1ca952"

def authenticate_youtube():
    """Authenticate to YouTube API using OAuth2."""
    # Specify the scopes
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    # Use the client_secret.json file downloaded from Google Cloud Console
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes)
    credentials = flow.run_console()

    # Build the YouTube service
    youtube = build("youtube", "v3", credentials=credentials)
    return youtube

def get_spotify_tracks(playlist_url):
    """Fetch track names and artists from a Spotify playlist."""
    auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    playlist_data = sp.playlist(playlist_id)
    tracks = []

    for item in playlist_data['tracks']['items']:
        track = item['track']
        track_name = track['name']
        artists = ", ".join(artist['name'] for artist in track['artists'])
        tracks.append(f"{track_name} {artists}")
    
    return tracks

def create_youtube_playlist(youtube, playlist_name, description=""):
    """Create a YouTube playlist."""
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": playlist_name,
                "description": description,
                "tags": ["music", "Spotify", "YouTube"],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"  # Set to "public" if desired
            }
        }
    )
    response = request.execute()
    return response["id"]

def search_youtube_video(youtube, query):
    """Search for a video on YouTube and return its video ID."""
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=query
    )
    response = request.execute()
    if response["items"]:
        return response["items"][0]["id"]["videoId"]
    return None

def add_video_to_youtube_playlist(youtube, playlist_id, video_id):
    """Add a video to a YouTube playlist."""
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    request.execute()

def download_mp3(query, output_dir="downloads"):
    """Download MP3 using youtube_dl."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': True,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([query])

def main():
    # Authenticate to YouTube
    print("Authenticating to YouTube...")
    youtube = authenticate_youtube()

    # Input Spotify playlist URL
    playlist_url = input("Enter Spotify playlist URL: ")
    
    # Fetch Spotify tracks
    print("Fetching Spotify playlist tracks...")
    tracks = get_spotify_tracks(playlist_url)
    print(f"Found {len(tracks)} tracks.")

    # Create YouTube playlist
    playlist_name = input("Enter name for the YouTube playlist: ")
    print("Creating YouTube playlist...")
    youtube_playlist_id = create_youtube_playlist(youtube, playlist_name)
    print(f"YouTube playlist created: {playlist_name}")

    # Add tracks to YouTube playlist and download MP3s
    print("Adding tracks to YouTube playlist and downloading MP3s...")
    for track in tracks:
        print(f"Processing track: {track}")

        # Search for the track on YouTube
        video_id = search_youtube_video(youtube, track)
        if video_id:
            # Add video to YouTube playlist
            add_video_to_youtube_playlist(youtube, youtube_playlist_id, video_id)

            # Download MP3
            youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            download_mp3(youtube_url)
            print(f"Downloaded: {track}")
        else:
            print(f"Track not found on YouTube: {track}")

    print("All tracks processed.")

if __name__ == "__main__":
    main()

