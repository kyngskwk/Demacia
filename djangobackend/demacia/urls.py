from django.urls import path
from . import views
from djangobackend import settings
from rest_framework import routers

app_name = 'demacia'

urlpatterns = [
    #챔피언추천
    path('recommand/<int:userno_pk>/champion', views.recommand_champion, name="recommand champion"),
    path('recommand/group', views.recommand_group, name="recommand group"),
    path('champions/', views.champion_list, name="champion list"),
    path('videoposts/', views.videopost_list, name="video list"),
    path('matches/', views.match_list, name="match list"),
    path('videoposts/<int:videopost_pk>/likes/list', views.videopostlike_list, name="videopostlike list"),
    path('videoposts/<int:videopost_pk>/likes/<int:userno_pk>', views.videopostlike_create_and_delete, name="videopostlike create and delete"),
    path('videoposts/<int:videopost_pk>/reply/<int:reply_pk>', views.replylike_list, name="replylike list"),
    path('videoposts/<int:videopost_pk>/reply/<int:reply_pk>', views.replylike_create_and_delete, name="replylike created and delete"),

]
