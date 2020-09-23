from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@api_view(['GET'])
def recommand_champion(request,userno_pk):
    matches = Match.objects.filter(userno=userno_pk)
    serializers = MatchSerializer(matches, many=True) 
    return Response(serializers.data)

@api_view(['GET'])
def recommand_group(request):
    # champions = Match.objects.values('recommand_champion') #{'티모':0.7,'아리':0.6,'럭스':0.3}
    user_champions = ['Annie','Olaf','Galio']
    group1 = Champion.objects.filter(chamname='Annie')
    group2 = Champion.objects.filter(chamname='Olaf')
    group3 = Champion.objects.filter(chamname='Olaf')
    response_data = {
        'First_cham': ChampionDictionarySerializer(group1, many=True).data,
        'Second_cham': ChampionDictionarySerializer(group2, many=True).data,
        'Third_cham' : ChampionDictionarySerializer(group3, many=True).data,
    }

    return Response(response_data)


@api_view(['GET'])
def champion_list(request):
    champions = Champion.objects.all() 
    serializers = ChampionSerializer(champions, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def videopost_list(request):
    videoposts = Videopost.objects.all()
    serializers = VideopostSerializer(videoposts, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def match_list(request):
    matches = Match.objects.all()
    serializers = MatchSerializer(matches, many=True)
    return Response(serializers.data)

@login_required
@api_view(['GET'])
def replylike_list(request):
    replylikes = Replylikes.objects.all()
    serializers = ReplylikesSerializer(replylieks, many=True)
    return Response(serializers.data)

@login_required
@api_view(['POST','DELETE'])
def replylike_create_and_delete(request):
    replylikes = Replylikes.objects.all()
    serializers = ReplylikesSerializer(replylieks, many=True)
    return Response(serializers.data)


@login_required
@api_view(['GET'])
def videopostlike_list(request):
    videopostlikes = Videopostlikes.objects.all()
    serializers = VideopostlikesSerializer(videopostlikes, many=True)
    return Response(serializers.data)

@login_required
@api_view(['POST','DELETE'])
def videopostlike_create_and_delete(request):
    videopostlikes = Videopostlikes.objects.all()
    serializers = VideopostlikesSerializer(videopostlikes, many=True)
    return Response(serializers.data)
