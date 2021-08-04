import json
import requests

class Track:

    def __init__(self, spotify_user_id, spotify_token, client_id, client_secret_id):
        
        self.user_id = spotify_user_id
        self.token = spotify_token
        self.client_id = client_id
        self.secret_id = client_secret_id
 
    def user(self):

        query = 'https://api.spotify.com/v1/users/{}/'.format(self.user_id)
        response = requests.get(query, headers={"Authorization": "Bearer {}".format(self.token)})
        response_json = response.json()

        if(response):
            user_name = response_json['display_name']
            photo_user = response_json['images'][0]['url']
            link_user = response_json['external_urls']['spotify']

            infos = {
                "username": user_name,
                "photo": photo_user,
                "link": link_user,
            }

            return infos

    def current_track(self):
        
        query = "https://api.spotify.com/v1/me/player/currently-playing"
        response = requests.get(query, headers={"Authorization": "Bearer {}".format(self.token)})

        if(response):
            response_json = response.json()
            track_id = response_json['item']['id']
            track_name = response_json['item']['name']
            artists = response_json['item']['artists']
            artists_name = ', '.join([artist['name'] for artist in artists])
            album_name = response_json['item']['album']['name']
            album_images = response_json['item']['album']['images']
            album_image_link = album_images[0]['url']

            current_track_info = {
                "id": track_id,
                "name": track_name,
                "artists": artists_name,
                "album": album_name,
                "album_image": album_image_link,
                "response": 1,
            }

            return current_track_info
        else:
            current_track_info = {
                "response": None
            }
            return current_track_info

# debug
# spotify_token = 'BQAa55OQSlHXjfAYiTM7u4ZULFSIhUgC3SyweUcXWaxhdwa5EN6f7cK8Tf5IzjtvXppLTQwGmDkDxa7lLO7UP_TaQuAxAxa0Lbmc2Q6DteuZZUAg6iCkQ3XLcoXOQQ7vC875lBjGjJUtlt2u46qIFBBNO_LOePgqtbI4LRxO-_asGuuGWCeWMr66M43K2REhwofiuEROqdv6b-ehJ8dJ1dxWI1sdEfmR1s_pzWdLZ4Ac1OH5GJXI67QkiTV38pVUdd7AQV9ajS7ui7PwRueXZ9LA'
# spotify_user_id = 'carloosxdd'
# client_id = 'a'
# secret_id= 'a'
# track = Track(spotify_user_id, spotify_token, client_id, secret_id)
# print(track.user())