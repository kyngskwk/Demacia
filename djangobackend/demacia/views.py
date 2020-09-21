from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ChampionSerializer
from .models import Champion
# Create your views here.

def test(request):
    return render(request, 'demacia/test.html')

@api_view(['GET'])
def champion_list(request):
    champions = Champion.objects.all()
    serializers = ChampionSerializer(champions, many=True)
    return Response(serializers.data)

