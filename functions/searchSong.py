from refreshOauthToken import RefreshOauth
import argparse, requests, json

class SearchSong:
    def __init__(self, client_id, client_secret, artist, song, refresh_token = "", oauth_token = ""):
        if refresh_token != "":
            self.access_token = RefreshOauth(refresh_token, client_id, client_secret).RequestAccessToken()
        else:
            self.access_token = oauth_token
        self.artist = artist
        self.song = song
        self.search_string = self.song + " " + self.artist

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

        response = requests.get(url=URL, headers=HEADERS,params=query_params).text
        
        result = json.loads(response)["tracks"]["items"]
        #print(result)

        popularity_sort = {}
        #found = False
        for x in result:
            popularity_sort[x["uri"]] = x["popularity"]
            if x["name"] == self.song and x["artist"][0]["name"] == self.artist:
                print("Found")
                found = True
                print(x["name"] + " -> " + x["artists"][0]["name"])

        most_close = result[0]["uri"]
        sorted_popularity = sorted(popularity_sort.items(), key=lambda x: x[1], reverse=True)
        
        if most_close:
            respo = open("response.txt", "w")
            print("MOST CLOSE -> " + most_close)
            respo.write(most_close)
            return most_close

        '''
        if not found:
            print("From popularity:")
            print(sorted_popularity[0][0])
            return sorted_popularity[0][0]
        '''
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Define parameters
    parser.add_argument("-id", "--client_id", required=True, help="Client ID of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-secret", "--client_secret", required=True, help="Client Secret of Spotify account, obtained from Spotify developer dashboard.")
    parser.add_argument("-token", "--refresh_token", required=True, help="Refresh token, obtained after authorization process.")
    parser.add_argument("-s", "--song", required=True, help="Search string for target song.")
    parser.add_argument("-a", "--artist", required=True, help="Search string for target artist.")


    args = vars(parser.parse_args())

    spotify_api = SearchSong(args["client_id"], args["client_secret"], args["artist"], args["song"], refresh_token=args["refresh_token"])

    search_result = spotify_api.searchSong()
