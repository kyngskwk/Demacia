from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

@api_view(['GET'])
def recommand_champion(request,userno):
    champions = Match.objects.filter(userno=userno)#{'티모':0.7,'아리':0.6,'럭스':0.3}
    serializers = MatchSerializer(champions, many=True) 
    #비슷한 성향을 가진 챔들
    return Response(serializers.data)

@api_view(['GET'])
def recommand_group(request,userno):
    champions = Match.objects.filter(userno=userno).values('recommand_champion')[0]['recommand_champion'] #{'티모':0.7,'아리':0.6,'럭스':0.3}
    json_champions = champions.replace("'","\"")
    groups = list(json.loads(json_champions).keys())

    group1 = Champion.objects.filter(chamkey=int(groups[0]))
    group2 = Champion.objects.filter(chamkey=int(groups[1]))
    group3 = Champion.objects.filter(chamkey=int(groups[2]))

    response_data = {
        'First_cham': ChampionSerializer(group1, many=True).data,
        'Second_cham': ChampionSerializer(group2, many=True).data,
        'Third_cham' : ChampionSerializer(group3, many=True).data,
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
def match_list(request,userno):
    matches = Match.objects.filter(userno=userno)
    serializers = MatchSerializer(matches, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def mbti_cham(request, user_mbti):
    mbti_chams = Champion.objects.filter(mbti=user_mbti)

    good_mbti = Champion.objects.filter(mbti=user_mbti).values('goodmbti').distinct()[0]['goodmbti']
    good_chams = Champion.objects.filter(mbti=good_mbti)

    bad_mbti = Champion.objects.filter(mbti=user_mbti).values('badmbti').distinct()[0]['badmbti']
    bad_chams = Champion.objects.filter(mbti=bad_mbti)

    mbti_serializers = ChampionSerializer(mbti_chams, many=True)
    bad_serializers = ChampionSerializer(bad_chams, many=True)
    good_serializers = ChampionSerializer(good_chams, many=True)

    response_data = {
        'mbti_chams': mbti_serializers.data,
        'bad_chams': bad_serializers.data,
        'good_chams': good_serializers.data
    }

    return Response(response_data)


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
