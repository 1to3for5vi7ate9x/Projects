import os
import subprocess
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

def download_spotify_playlist(playlist_url, batch_size=100, output_dir="downloads"):
    # Spotify API credentials
    CLIENT_ID = "5a60b1d47daf479aa928d62888bd1787"
    CLIENT_SECRET = "b2d5dc22b238439ab3709a5a2f1ca952"

    # Authenticate with Spotify
    auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = Spotify(auth_manager=auth_manager)

    # Extract playlist ID from the URL
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    # Fetch playlist details
    playlist_data = sp.playlist(playlist_id)
    playlist_name = playlist_data['name']
    total_tracks = playlist_data['tracks']['total']
    print(f"Playlist: {playlist_name}")
    print(f"Total tracks: {total_tracks}")

    # Create a directory for the playlist
    playlist_dir = os.path.join(output_dir, playlist_name)
    if not os.path.exists(playlist_dir):
        os.makedirs(playlist_dir)

    # Fetch and process tracks in batches
    offset = 0
    while offset < total_tracks:
        print(f"Fetching tracks {offset + 1} to {min(offset + batch_size, total_tracks)}...")
        tracks = sp.playlist_tracks(playlist_id, offset=offset, limit=batch_size)

        for item in tracks['items']:
            track = item['track']
            track_name = track['name']
            artists = ", ".join(artist['name'] for artist in track['artists'])
            query = f"{track_name} {artists}"
            print(f"Downloading: {track_name} by {artists}")

            # Use spotdl to download the track
            try:
                subprocess.run(
                    ["spotdl", "download", query, "--output", playlist_dir],
                    check=True,
                )
            except subprocess.CalledProcessError as e:
                print(f"Failed to download: {query}, Error: {e}")

        offset += batch_size

    print("Download complete.")

if __name__ == "__main__":
    playlist_url = input("Enter the Spotify playlist URL: ")
    download_spotify_playlist(playlist_url)

