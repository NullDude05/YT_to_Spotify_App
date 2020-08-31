import os
import requests
import sys
import json
import spotipy
import spotipy.util as util
import search

# User ID: 
username = 'this can be your spotify username'
playlistid = ''
songid = ''
songs = []
# s = search.Search()

# Call environment user variables i.e. client id, client secret, and redirect uri
clientid = os.environ['SPOTIPY_CLIENT_ID']
secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirecturi = os.environ['SPOTIPY_REDIRECT_URI']

try:
    token = util.prompt_for_user_token(username,
        client_id=clientid,
        client_secret=secret,
        redirect_uri=redirecturi)
except:
    os.remove(f'.cache-{username}')

    token = util.prompt_for_user_token(username,
        scope='playlist-modify-public',
        client_id=clientid,
        client_secret=secret,
        redirect_uri=redirecturi)

#Create spotify object
sp = spotipy.Spotify(auth=token)

def checkplaylistnames():
    playlists = sp.user_playlists(username)
    # print(json.dumps(playlists, sort_keys=True, indent=4))

    for items in playlists['items']:
        return items['name']

    #     if playlistname in items['name']:
    #         return True
    
    # return False
            
def findplaylistid(name):
    playlists = sp.user_playlists(username)

    for items in playlists['items']:
        if name in items['name']:
            return items['id']



def getplaylist(playlistname):
    name = checkplaylistnames()
    playlistid = findplaylistid(name)

    
    return str(playlistid)

def addtracks(playlistid):
    sp.user_playlist_add_tracks(username, playlistid, songs)
    # print('Ode to the mets has been added')


def createplaylist(playlistname, description):

    checker = checkplaylistnames()

    if playlistname in checker:
        print('playlist has already been created dumb dumb')
    else:
        sp.user_playlist_create(username, playlistname, public=True, description=description)
        print('playlist has now been created')


def SearchSong(songtrack, artistname):
    song = sp.search(songtrack, type='track')

    for tracks in song['tracks']['items']:
        for item in tracks['artists']:
            if item['name'].lower() == artistname.lower():
                print('thispassed')
                songid = item['id']
                # break
        else:
            continue

    return songid

def startscript():
    playlist_name = 'Automated Playlist'
    description = 'Automated playlist i created lol'

    createplaylist(playlist_name, description)
    playlistid = getplaylist(playlist_name)

    # songtrack = input('Song Name: ')
    # artistname = input('Artist Name: ')

    # dataid = SearchSong(songtrack, artistname)
    # songs.append(dataid)
    

    # for tracks in song['tracks']['items']:
    #     for item in tracks['artists']:
    #         if item['name'].lower() == artistname:
    #             print('thispassed')
            # if item['artists']['name'].lower() == 'the strokes':
            #     songid = item['id']
            #     songs.append(songid)
            # else:
            #     continue



    # addtracks(playlistid)
    

startscript()