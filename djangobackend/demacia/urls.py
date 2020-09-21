from django.urls import path
from . import views
from djangobackend import settings
from rest_framework import routers

app_name = 'demacia'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('champions/', views.champion_list, name="list"),
]