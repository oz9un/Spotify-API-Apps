from functions.refreshOauthToken import RefreshOauth
from functions.searchSong import SearchSong
from functions.addTrackToPlaylist import AddSong

import argparse

class AddMyFavoriteSong:
  def __init__(self, client_id, client_secret, refresh_token, song, artist, playlist):
    self.CLIENT_ID = client_id
    self.CLIENT_SECRET = client_secret
    self.REFRESH_TOKEN = refresh_token
    self.song = song
    self.artist = artist
    self.playlist = playlist

  def get_OAuthToken(self):
    oauth_refresher = RefreshOauth(self.REFRESH_TOKEN, self.CLIENT_ID, self.CLIENT_SECRET)
    self.OAUTH_TOKEN = oauth_refresher.RequestAccessToken()

  def get_trackID(self):
    trackid_getter = SearchSong(self.CLIENT_ID, self.CLIENT_SECRET, self.artist, self.song, refresh_token="", oauth_token=self.OAUTH_TOKEN)
    self.TRACK_ID = trackid_getter.searchSong()

  def add_track(self):
    track_adder = AddSong(self.playlist, self.TRACK_ID, self.OAUTH_TOKEN)
    track_adder.add_song()

  def run_all(self):
    # Get a new OAuth token using refresh token:
    self.get_OAuthToken()
    
    # Get your favorite song's track id:
    self.get_trackID()

    # Add your favorite song to target playlist:
    self.add_track()
  

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Define parameters
    parser.add_argument("-id", "--client_id", required=True, help="Client ID of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-secret", "--client_secret", required=True, help="Client Secret of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-token", "--refresh_token", required=True, help="Refresh token, obtained after authorization process.")
    parser.add_argument("-s", "--song", required=True, help="Search string for target song.")
    parser.add_argument("-a", "--artist", required=True, help="Search string for target artist.")
    parser.add_argument("-p", "--playlist", required=True, help="Target playlist for our favorite song.")


    args = vars(parser.parse_args())

    spotify_api = AddMyFavoriteSong(args["client_id"], args["client_secret"], args["refresh_token"], args["song"], args["artist"], args["playlist"])
    
    try:
      spotify_api.run_all()
    except:
      f = open("failed_operation", "w")
      f.write("oopps. try again")

