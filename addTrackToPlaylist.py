import requests, argparse

class AddSong:
  def __init__(self, playlist_id, track_id, oauth_token):
    self.playlist_id = playlist_id
    self.track_id = track_id
    self.oauth_token = oauth_token

  def add_song(self):
    URL = "https://api.spotify.com/v1/playlists/{pid}/tracks".format(pid=self.playlist_id)
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + self.oauth_token
    }
    query_params = {
        "uris": self.track_id
    }

    response = requests.post(url=URL, headers=HEADERS, params=query_params).text
    print(response)

if __name__ == '__main__':

  parser = argparse.ArgumentParser()

  # Define parameters
  parser.add_argument("-p", "--playlist", required=True, help="Target playlist id.")
  parser.add_argument("-t", "--track", required=True, help="Target track id.")
  parser.add_argument("-token", "--oauth_token", required=True, help="Oauth token, obtained with refresh token.")


  args = vars(parser.parse_args())
  args["playlist"], args["track"], args["oauth_token"]
  song_adder = AddSong(args["playlist"], args["track"], args["oauth_token"])
  song_adder.add_song()


