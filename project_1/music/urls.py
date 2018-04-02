from . import views # . means look at current directory
from django.conf.urls import  url

urlpatterns = [
    url(r'^$',views.index, name='index'), #path doesnot support regular exp
]
