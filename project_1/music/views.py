from django.shortcuts import render
from .models import Album,Song

from django.http import HttpResponse
from django.shortcuts import  render
from django.http import Http404

# Create your views here.


def index(request):
    all_album = Album.objects.all();
    #context used to share data to template
    context = {
                'all_album': all_album,
              }
    return render(request, 'music/index.html', context)


def details(request,album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('Album Does not Exist')
    return render(request,'music/details.html',{'album':album})

def home(request):
    return render(request, 'home.html', {})