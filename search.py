# import spotipy
# import spotipy.util as util
# import os
# import json



# clientid = os.environ['SPOTIPY_CLIENT_ID']
# secret = os.environ['SPOTIPY_CLIENT_SECRET']
# redirecturi = os.environ['SPOTIPY_REDIRECT_URI']

# try:
#     token = util.prompt_for_user_token(username,
#         client_id=clientid,
#         client_secret=secret,
#         redirect_uri=redirecturi)
# except:
#     os.remove(f'.cache-{username}')

#     token = util.prompt_for_user_token(username,
#         scope='playlist-modify-public',
#         client_id=clientid,
#         client_secret=secret,
#         redirect_uri=redirecturi)

# sp = spotipy.Spotify(auth=token)

# class Search:
#     def __init__(self):
#         pass

#     def SearchSong(self):
#         songtrack = input('Song Name: ')
#         artistname = input('Artist Name: ')

#         song = sp.search(songtrack, type='track')

#         return song


# if __name__ == '__main__':
#     Search()