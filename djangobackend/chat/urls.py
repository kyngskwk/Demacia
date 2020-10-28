from django.urls import path
from . import views
from djangobackend import settings
from rest_framework import routers
from django.conf.urls.static import static

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('<room_name>/', views.room, name='room'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)