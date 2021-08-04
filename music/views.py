from django.shortcuts import render
from django.http import HttpResponse, response
from . import ctrack

def index(request):
    if request.method == 'POST':

        token = request.POST['token']
        client_id = request.POST['clientid']
        client_secret_id = request.POST['secrectid']
        spotify_user_id = request.POST['spid'] 

        rp = ctrack.Track(spotify_user_id, token, client_id , client_secret_id)

        current_track_info = rp.current_track()
        user = rp.user()

        return render(request, 'index.html', current_track_info, user)
    else:

        token = 'a'
        client_id = 'a'
        client_secret_id = 'a'
        spotify_user_id = 'a'

        rp = ctrack.Track(spotify_user_id, token, client_id , client_secret_id)
        current_track_info = rp.current_track()

        user = rp.user()

        return render(request, 'index.html', current_track_info, user)