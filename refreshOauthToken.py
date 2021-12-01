import requests, json, base64, sys

class SpotifyAPI:
    def __init__(self, refresh_token, client_id, client_secret):
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret

    def RequestAccessToken(self):
        URL = "https://accounts.spotify.com/api/token"
        HEADERS = {
            "Authorization":"Basic {}".format(base64.b64encode(self.client_id+":"+self.client_secret)),
            "Content-Type":"application/x-www-form-urlencoded",
        }
        body_data = {
            "grant_type":"refresh_token",
            "refresh_token":self.refresh_token,
            "redirect_uri":"https://ozgunkultekin.com"
        }
        response = requests.post(url=URL, headers=HEADERS,data=body_data)
        return json.loads(response.text)


if __name__ == '__main__':
    client_id = sys.argv[1]
    client_secret = sys.argv[2]
    refresh_token = sys.argv[3]
    spotify_api = SpotifyAPI(refresh_token, client_id, client_secret)
