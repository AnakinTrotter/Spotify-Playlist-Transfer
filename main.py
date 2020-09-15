import secrets
import spotify_client

# 31ovnqeyxbqbyw3tgxi3ey2flgwu
# lf7getu0uxe4ycr73nwvvvo6n

def run():
    source_user = ""
    dest_user = ""

    print("\n\n\n")
    print("Spotify Playlist Transfer will take all the playlists from the source account and copy them to the "
          "destination account.")
    print("Reading and creating playlists requires account authorization which may involve pasting the link you are "
          "redirected to into the program.")
    source_user = input("Source Username: ").strip()
    dest_user = input("Destination Username:").strip()

    secrets.set_secret_envs()
    spotify_client.get_playlists(source_user)
    spotify_client.create_playlists(dest_user)



if __name__ == "__main__":
    run()
