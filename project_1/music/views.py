from django.shortcuts import render
from .models import Album,Song

from django.http import HttpResponse
from django.template import  loader

# Create your views here.


def index(request):
    all_album = Album.objects.all();
    template = loader.get_template('music/index.html')

    #context used to share data to template
    context = {
                'all_album': all_album,
              }
    return HttpResponse(template.render(context,request))


def details(request,album_id):
    return HttpResponse("<h2>Details for Album : "+str(album_id)+"</h2>")


