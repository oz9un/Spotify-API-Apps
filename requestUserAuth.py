import sys, requests, json, argparse

class SpotifyAPI:
    def __init__(self, client_id, redirect_uri):
        self.client_id = client_id
        self.redirect_uri = redirect_uri

    def refreshTokenGenerator(self):
        URL = "https://accounts.spotify.com/authorize"

        query_parameters = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
        }
        response = requests.get(url=URL, params=query_parameters, allow_redirects=True)
        print(response.text)


if __name__ == '__main__':
    # Get user parameters:
    parser = argparse.ArgumentParser()

    # Define parameters
    parser.add_argument("-id", "--client_id", required=True, help="Client ID of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-uri", "--redirect_uri", required=True, help="Redirect URI, place that refresh token will send to. (set localhost!)")

    args = vars(parser.parse_args())

    spotify_api = SpotifyAPI(args["client_id"], args["redirect_uri"])
    spotify_api.refreshTokenGenerator()