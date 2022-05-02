import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import configparser
import spotipy.oauth2 as oauth2

config = configparser.ConfigParser()
config.read('config.cfg')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
client_redirect = config.get('SPOTIFY', 'REDIRECT_URI')


class Spotify:
    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=client_redirect, scope=scope))
    results = sp.current_user_saved_tracks()

    music = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        row = (track['artists'][0]['name'], item['track'], track['name'])
        music.append(row)
        print(idx, track['artists'][0]['name'], " – ", track['name'])
