from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
print("CLIENT_ID:", CLIENT_ID)  # Debugging line to check if CLIENT_ID is set
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
print(
    "CLIENT_SECRET:", CLIENT_SECRET
)  # Debugging line to check if CLIENT_SECRET is set

year = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)

URL = f"https://www.billboard.com/charts/hot-100/{year}"
print(URL)

response = requests.get(url=URL)
html_response = response.text

soup = BeautifulSoup(html_response, "html.parser")

song_elements = soup.select("li ul li h3")


songs = [song.getText(strip=True) for song in song_elements]

filtered_songs = [
    title for title in songs if title and not title.endswith(":") and len(title) > 2
]

# Authenticate with Spotify
my_spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-private",
        cache_path="token.txt",
        show_dialog=True,
    )
)

# Get user ID
user_id = my_spotify.current_user()["id"]

year = year.split("-")[0]
songs_uris = []

for song in filtered_songs:
    result = my_spotify.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        songs_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new playlist
playlist = my_spotify.user_playlist_create(
    user=user_id,
    name=f"{year} Billboard 100",
    public=False,
    description=f"Top 100 songs from Billboard Hot 100 in {year}",
)

# Add songs to the playlist
my_spotify.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)
print(f"Playlist created: {playlist['external_urls']['spotify']}")
