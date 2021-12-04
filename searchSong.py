from refreshOauthToken import SpotifyAPI
import argparse, requests, json

class SearchSong:
    def __init__(self, refresh_token, client_id, client_secret, artist, song):
        self.access_token = SpotifyAPI(refresh_token, client_id, client_secret).RequestAccessToken()
        self.artist = artist
        self.song = song

    def searchSong(self):
        URL = "https://api.spotify.com/v1/search"
        HEADERS = {
            "Authorization": "Bearer {}".format(self.access_token),
            "Content-Type": "application/json",
        }
        query_params = {
            "q": self.song,
            "type": "track",
        }

        response = requests.get(url=URL, headers=HEADERS,params=query_params).text
        
        result = json.loads(response)["tracks"]["items"]

        popularity_sort = {}
        found = False
        for x in result:
            popularity_sort[x["uri"]] = x["popularity"]
            if x["name"] == args["song"] and x["artist"][0]["name"] == args["artist"]:
                print("Found")
                found = True
                print(x["name"] + " -> " + x["artists"][0]["name"])
        
        sorted_popularity = sorted(popularity_sort.items(), key=lambda x: x[1], reverse=True)
        
        if not found:
            print("From popularity:")
            print(sorted_popularity[0][0])
            return sorted_popularity[0][0]
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Define parameters
    parser.add_argument("-id", "--client_id", required=True, help="Client ID of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-secret", "--client_secret", required=True, help="Client Secret of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-token", "--refresh_token", required=True, help="Refresh token, obtained after authorization process.")
    parser.add_argument("-s", "--song", required=True, help="Search string for target song.")
    parser.add_argument("-a", "--artist", required=True, help="Search string for target artist.")


    args = vars(parser.parse_args())

    spotify_api = SearchSong(args["refresh_token"], args["client_id"], args["client_secret"], args["artist"], args["song"])

    search_result = spotify_api.searchSong()
