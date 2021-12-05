# Spotify-Token-Generator 🎷🎶 🎼
This repository represents my efforts for Python implementation of Spotify's authorization flow.

# Still developing...
![gif](https://media2.giphy.com/media/XzqEFZ06NSFgXaut2g/giphy.gif?cid=ecf05e475dsps2ksk27bc60tgkzdfz4e20d92tj6enoq4wes&rid=giphy.gif&ct=g)


## To-do:
- requestUserAuth.py don't follow the redirections yet, will be fixed.
- Search Song creates token with 'modify-playlist-private' scope. It's just overkill for now. Will fix.

## searchSong:
- Search Song uses 'refreshOauthToken' for new token generation.
- It requires two inputs from user:
    - Artist's name
    - Song's name

- It returns most searched one about that keywords.
- It also can sort songs by their popularities.
