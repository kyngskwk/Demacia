from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
# Create your views here.

def test(request):
    return render(request, 'demacia/test.html')

@api_view(['GET'])
def champion_list(request):
    champions = Champion.objects.all()
    serializers = ChampionSerializer(champions, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def videopost_list(request):
    videoposts = VideoPost.objects.all()
    serializers = VideoPostSerializer(videoposts, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def match_list(request):
    matches = Match.objects.all()
    serializers = MatchSerializer(matches, many=True)
    return Response(serializers.data)

