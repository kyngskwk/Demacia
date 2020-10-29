from django.conf.urls import url
from . import views
from djangobackend import settings
from rest_framework import routers
from django.conf.urls.static import static

app_name = 'chat'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)