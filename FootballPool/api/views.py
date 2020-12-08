from django.shortcuts import render
from api.models import Game
import requests
import json

# Create your views here.
def home(request):
    return render(request,'api/scores.html')
