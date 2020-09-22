from .models import Champion, VideoPost , Match, ReplyLikes , VideoPostLikes
from rest_framework import serializers, viewsets
# Seriallizer는 API를 통한 요청에 대한 응답의 형태를을 결정해주는 클래스이다. 
# ViewSet은 요청을 처리하여 응답을 해주는 클래스이다. 
# 이곳에 get, post, put, patch, delete에 대한 액션을 지정

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = '__all__'

class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPost
        fields = '__all__'    

class VideoPostViewSet(viewsets.ModelViewSet):
    queryset = VideoPost.objects.all()
    serializer_class =  VideoPostSerializer
 
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'   

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class =  MatchSerializer

class ReplyLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyLikes
        fields = '__all__'   

class ReplyLikesViewSet(viewsets.ModelViewSet):
    queryset = ReplyLikes.objects.all()
    serializer_class =  ReplyLikesSerializer

class VideoPostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPostLikes
        fields = '__all__'   

class VideoPostLikesViewSet(viewsets.ModelViewSet):
    queryset = VideoPostLikes.objects.all()
    serializer_class =  VideoPostLikesSerializer