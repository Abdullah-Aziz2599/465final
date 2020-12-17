from django.shortcuts import render, redirect
from scores.forms import SubmissionForm
from core.models import League, UserProfile
from django.forms import formset_factory
from api.models import Game
from scores.models import UserSelection
# Create your views here.


def form_submission(request):
    context = {'games':[], 'leagues':[]}
    games = Game.objects.all()
    context['games'] = games
    num_of_game = games.count()
    if request.method == 'POST' and 'submit_form' in request.POST:
        for game in games:
            choice = request.POST.get(game.game_id)
            UserSelection(user = request.user, team_selected = choice).save()
            print(choice)
        user = UserProfile.objects.get(user = request.user)
        user.form_submit = True
        user.save()
        leagues = League.objects.all()
        for league in leagues:
            if request.user in league.league_members.all():
                context['leagues'].append(league)
        return redirect('/')
    elif request.method == 'GET' and 'cancel' in request.POST:
        leagues = League.objects.all()
        for league in leagues:
            if request.user in league.league_members.all():
                context['leagues'].append(league)
        return redirect('/')
    leagues = League.objects.all()
    for league in leagues:
        if request.user in league.league_members.all():
            context['leagues'].append(league)
    return render(request, 'scores/form_submission.html', context)
