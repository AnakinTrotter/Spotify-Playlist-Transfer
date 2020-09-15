import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = "user-library-read playlist-read-private playlist-read-collaborative playlist-modify-public " \
        "playlist-modify-private user-library-modify user-follow-read user-follow-modify"


def get_playlists(username):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, scope=scope, show_dialog=True))

    playlists = sp.user_playlists(username)
    for i in range(0, len(playlists['items'])):
        offset = 0
        playlist_uri = playlists['items'][i]['uri']
        playlist_info = playlists['items'][i]
        playlist_uri = playlist_uri.replace(":", ";")
        playlist_file = open(file="Library/Playlists/" + playlist_uri, mode="w+", encoding="utf-8")
        playlist_uri = playlist_uri.replace(";", ":")
        playlist_file.write(playlist_info['name'] + "\n")
        playlist_file.write(str(playlist_info['public']) + "\n")
        playlist_file.write(str(playlist_info['collaborative']) + "\n")
        playlist_file.write(playlist_info['description'] + "\n")
        while True:
            playlist = sp.playlist_items(playlist_id=playlist_uri, offset=offset)
            track_num = len(playlist['items'])
            for j in range(0, track_num):
                playlist_file.write(playlist['items'][j]['track']['uri'] + "\n")
            if track_num < 100:
                break
            offset += 100
        playlist_file.close()


def create_playlists(username):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, scope=scope, show_dialog=True))

    for playlist in os.listdir("Library/Playlists/"):
        playlist_file = open("Library/Playlists/" + playlist)
        name = playlist_file.readline()
        public = playlist_file.readline()
        collaborative = playlist_file.readline()
        description = playlist_file.readline()
        spotify_playlist = sp.user_playlist_create(username, name, public, collaborative, description)
        spotify_playlist = "spotify:playlist:" + spotify_playlist['id']
        tracks = playlist_file.read()
        tracks = tracks.split("\n")
        tracks.remove("")
        while len(tracks) >= 100:
            sp.playlist_add_items(spotify_playlist, tracks[0:100])
            tracks = tracks[100:len(tracks)]
        sp.playlist_add_items(spotify_playlist, tracks)
