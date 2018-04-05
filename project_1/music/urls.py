from . import views # . means look at current directory
from django.conf.urls import  url

app_name='music' #nameSpacing

urlpatterns = [
    url(r'^$',views.index, name='index'), #path doesnot support regular exp

    #music/1 where 1 is id
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='detail'),

    # music/id/favorite
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
