from django.shortcuts import render
from .models import Album,Song


from django.shortcuts import  render,get_object_or_404
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
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/details.html',{'album':album})


#def home(request):
 #   return index(request)
    #return render(request, 'home.html', {})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        print("\n\n\n" + request.POST['song'] + "\n\n\n\n")

        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return(request, 'music/details.html', {
                            'album': album,
                            'error_message': "You Did not select amy options",
                             })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})
