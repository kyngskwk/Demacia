from django.urls import path
from . import views
from djangobackend import settings
from rest_framework import routers

app_name = 'demacia'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('champions/', views.champion_list, name="champion list"),
    path('videoposts/', views.videopost_list, name="video list"),
    path('matches/', views.match_list, name="match list"),
    path('videopostlikes/', views.videopostlike_list, name="videopostlike list"),
    path('videopostlikes/<int:videopost_pk>', views.videopostlike_delete, name="videopostlike delete"),
    path('videopostlikes/<int:videopost_pk>', views.videopostlike_create, name="videopostlike create"),
    path('replylikes/', views.replylike_list, name="replylike list"),
    path('replylikes/<int:reply_pk>', views.replylike_delete, name="replylike delete"),
    path('replylikes/<int:reply_pk>', views.replylike_create, name="replylike create"),

]