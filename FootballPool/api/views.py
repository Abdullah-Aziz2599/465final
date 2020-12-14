from django.shortcuts import render
from api.models import Game
import requests
import json
from datetime import datetime
from pytz import timezone
import pytz

# Create your views here.
def home(request):
    # Game.objects.all().delete()
    # date_format = "%Y-%m-%d"
    # date = datetime.now(tz=pytz.utc)
    # date = date.astimezone(timezone('US/Pacific'))
    # date = date.strftime(date_format)
    # print(date)
    # context = {'games': [], 'is_there_scoreboard':False}
    # is_there_scoreboard = False
    # game_date = ""
    # ext = ".png"
    # url = "https://sportspage-feeds.p.rapidapi.com/games"
    #
    # querystring = {"league":"NFL", "date": date}
    #
    # headers = {
    #     'x-rapidapi-key': "3d8c589af3msh9693745514aae90p10db67jsnd22121612369",
    #     'x-rapidapi-host': "sportspage-feeds.p.rapidapi.com"
    # }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # json_data = json.loads(response.text)
    # num_of_games = 0
    # num_of_games =  json_data["games"]
    # for i in range(0,num_of_games):
    #     for info in json_data["results"][i]:
    #         if info == "schedule":
    #             game_date = json_data["results"][i]["schedule"]["date"]
    #             game_date = game_date.split("T")
    #             game_date = game_date[0]
    #         if info == "teams":
    #             away_team = json_data["results"][i]["teams"]["away"]["team"]
    #             home_team = json_data["results"][i]["teams"]["home"]["team"]
    #             away_team_image = away_team + ext
    #             home_team_image = home_team + ext
    #         if info == "scoreboard":
    #             away_score = json_data["results"][i]["scoreboard"]["score"]["away"]
    #             home_score = json_data["results"][i]["scoreboard"]["score"]["home"]
    #             current_period = json_data["results"][i]["scoreboard"]["currentPeriod"]
    #             time_remaining = json_data["results"][i]["scoreboard"]["periodTimeRemaining"]
    #             context['is_there_scoreboard'] = True
    #     if context['is_there_scoreboard'] == True:
    #         Game(home_team = home_team, away_team = away_team, away_score = away_score, home_score = home_score, current_period = current_period, time_remaining = time_remaining, home_team_image = home_team_image, away_team_image = away_team_image,game_date = game_date).save()
    #     else:
    #         Game(home_team = home_team, away_team = away_team, away_score = -1, home_score = -1, current_period = -1, time_remaining = "-1", home_team_image = home_team_image, away_team_image = away_team_image, game_date = game_date).save()
    # game = Game.objects.all()
    # context['games'] = game
    return render(request,'api/scores.html')
