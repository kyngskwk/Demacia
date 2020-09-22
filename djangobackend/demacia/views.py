from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required
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

@login_required
@api_view(['GET'])
def replylike_list(request):
    replylikes = ReplyLikes.objects.all()
    serializers = ReplyLikesSerializer(replylieks, many=True)
    return Response(serializers.data)

@login_required
@api_view(['POST'])
def replylike_create(request):
    replylikes = ReplyLikes.objects.all()
    serializers = ReplyLikesSerializer(replylieks, many=True)
    return Response(serializers.data)

@login_required
@api_view(['DELETE'])
def replylike_delete(request):
    replylikes = ReplyLikes.objects.all()
    serializers = ReplyLikesSerializer(replylieks, many=True)
    return Response(serializers.data)

@login_required
@api_view(['GET'])
def videopostlike_list(request):
    videopostlikes = VideoPostLikes.objects.all()
    serializers = VideoPostLikesSerializer(videopostlikes, many=True)
    return Response(serializers.data)

@login_required
@api_view(['POST'])
def videopostlike_create(request):
    videopostlikes = VideoPostLikes.objects.all()
    serializers = VideoPostLikesSerializer(videopostlikes, many=True)
    return Response(serializers.data)

@login_required
@api_view(['DELETE'])
def videopostlike_delete(request):
    videopostlikes = VideoPostLikes.objects.all()
    serializers = VideoPostLikesSerializer(videopostlikes, many=True)
    return Response(serializers.data)