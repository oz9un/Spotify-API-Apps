import requests, json, base64, sys, argparse

class RefreshOauth:
    def __init__(self, refresh_token, client_id, client_secret):
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret

    def RequestAccessToken(self):
        URL = "https://accounts.spotify.com/api/token"
        HEADERS = {
            "Authorization":"Basic {}".format(base64.b64encode((self.client_id+":"+self.client_secret).encode()).decode()),
            "Content-Type":"application/x-www-form-urlencoded",
        }
        body_data = {
            "grant_type":"refresh_token",
            "refresh_token":self.refresh_token,
            "redirect_uri":"https://ozgunkultekin.com"
        }
        response = requests.post(url=URL, headers=HEADERS,data=body_data)
        return json.loads(response.text)["access_token"]


if __name__ == '__main__':
    # Get user parameters:
    parser = argparse.ArgumentParser()

    # Define parameters
    parser.add_argument("-id", "--client_id", required=True, help="Client ID of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-secret", "--client_secret", required=True, help="Client Secret of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-token", "--refresh_token", required=True, help="Refresh token, obtained after authorization process.")

    args = vars(parser.parse_args())

    spotify_api = RefreshOauth(args["refresh_token"], args["client_id"], args["client_secret"])

    access_token = spotify_api.RequestAccessToken()
    print("Your new access token is: " + access_token)