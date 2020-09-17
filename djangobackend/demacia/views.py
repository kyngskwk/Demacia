from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

def test(request):
    return render(request, 'demacia/test.html')