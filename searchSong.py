from refreshOauthToken import SpotifyAPI
import argparse, requests, json

class SearchSong:
    def __init__(self, refresh_token, client_id, client_secret, search_string):
        self.access_token = SpotifyAPI(refresh_token, client_id, client_secret).RequestAccessToken()
        self.search_string = search_string

    def searchSong(self):
        URL = "https://api.spotify.com/v1/search"
        HEADERS = {
            "Authorization": "Bearer {}".format(self.access_token),
            "Content-Type": "application/json",
        }
        query_params = {
            "q": self.search_string,
            "type": "track",
        }

        response = requests.get(url=URL, headers=HEADERS,params=query_params)
        return response.text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Define parameters
    parser.add_argument("-id", "--client_id", required=True, help="Client ID of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-secret", "--client_secret", required=True, help="Client Secret of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-token", "--refresh_token", required=True, help="Refresh token, obtained after authorization process.")
    parser.add_argument("-s", "--search", required=True, help="Search string for target song.")


    args = vars(parser.parse_args())

    spotify_api = SearchSong(args["refresh_token"], args["client_id"], args["client_secret"], args["search"])

    search_result = spotify_api.searchSong()
    print(json.loads(search_result)["tracks"])