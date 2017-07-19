
from django.conf.urls import url
from django.contrib import admin

from . views import(
    home,
    node_api
)


urlpatterns = [
        url(r'^home/$', home, name='home'),
        url(r'^node_api/$', node_api, name='node_api'),
        
]
