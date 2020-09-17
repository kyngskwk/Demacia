from django.urls import path
from . import views
from djangobackend import settings

app_name = 'demacia'

urlpatterns = [
    path('test/', views.test, name='test')
    
]