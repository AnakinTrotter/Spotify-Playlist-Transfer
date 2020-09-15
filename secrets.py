import os

CLIENT_ID = "1183c40d682a46a183ed0ea3c06cd1d3"
CLIENT_SECRET = "86d2cdbd6b4f44b19efc440a7bb81c8c"
REDIRECT_URI = "http://blank.org/"


def set_secret_envs():
    os.environ["SPOTIPY_CLIENT_ID"] = CLIENT_ID
    os.environ["SPOTIPY_CLIENT_SECRET"] = CLIENT_SECRET
    os.environ["SPOTIPY_REDIRECT_URI"] = REDIRECT_URI
