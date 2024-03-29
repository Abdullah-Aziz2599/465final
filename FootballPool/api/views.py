from django.shortcuts import render
from api.models import Game
import requests
import json
from datetime import datetime, timedelta
from pytz import timezone
from core.models import League
import pytz
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import GameSerializer, UserSerializer

# Create your views here.


def home(request):
    Game.objects.all().delete()
    presentday = datetime.now()
    tomorrow = presentday + timedelta(1)
    tomorrow = tomorrow.strftime('%Y-%m-%d')
    date_format = "%Y-%m-%d"
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    date = date.strftime(date_format)
    print(date)
    context = {'games': [], 'is_there_scoreboard': False, "leagues": []}
    is_there_scoreboard = False
    game_date = ""
    ext = ".png"
    url = "https://sportspage-feeds.p.rapidapi.com/games"

    querystring = {"league": "NFL", "date": tomorrow}

    headers = {
        'x-rapidapi-key': "3d8c589af3msh9693745514aae90p10db67jsnd22121612369",
        'x-rapidapi-host': "sportspage-feeds.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    num_of_games = 0
    num_of_games = json_data["games"]
    for i in range(0, num_of_games):
        for info in json_data["results"][i]:
            if info == "schedule":
                game_date = json_data["results"][i]["schedule"]["date"]
                game_date = game_date.split("T")
                game_date = game_date[0]
            if info == "teams":
                away_team = json_data["results"][i]["teams"]["away"]["team"]
                home_team = json_data["results"][i]["teams"]["home"]["team"]
                away_team_image = away_team + ext
                home_team_image = home_team + ext
            if info == "scoreboard":
                away_score = json_data["results"][i]["scoreboard"]["score"]["away"]
                home_score = json_data["results"][i]["scoreboard"]["score"]["home"]
                current_period = json_data["results"][i]["scoreboard"]["currentPeriod"]
                time_remaining = json_data["results"][i]["scoreboard"]["periodTimeRemaining"]
                context['is_there_scoreboard'] = True
        if context['is_there_scoreboard'] == True:
            temp = i + 1
            game_id = str(temp)
            Game(home_team=home_team, away_team=away_team, away_score=away_score, home_score=home_score, current_period=current_period,
                 time_remaining=time_remaining, home_team_image=home_team_image, away_team_image=away_team_image, game_date=game_date, game_id=game_id).save()
        else:
            temp = i + 1
            game_id = str(temp)
            Game(home_team=home_team, away_team=away_team, away_score=-1, home_score=-1, current_period=-1, time_remaining="-1",
                 home_team_image=home_team_image, away_team_image=away_team_image, game_date=game_date, game_id=game_id).save()
    game = Game.objects.all()
    context['games'] = game
    leagues = League.objects.all()
    for league in leagues:
        if request.user in league.league_members.all():
            context['leagues'].append(league)
            print("True")
    return render(request, 'api/scores.html', context)


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tasks to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
