from django.shortcuts import render, redirect
from core.forms import JoinForm, LoginForm, CreateLeagueForm, JoinLeague, EditSettings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.models import UserProfile, League
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from feed.models import FeedItem
import requests
import json
from django.contrib import messages


@login_required(login_url='/login/')
def home(request):
    context = {'leagues': []}
    leagues = League.objects.all()
    for league in leagues:
        if request.user in league.league_members.all():
            context['leagues'].append(league)
            print("True")
    return render(request, "core/home.html", context)
def about(request):
    context = {"leagues":[]}
    leagues = League.objects.all()
    for league in leagues:
        if request.user in league.league_members.all():
            context['leagues'].append(league)
            print("True")
    return render(request, "core/about.html", context)


def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            user = join_form.save()
            UserProfile.objects.create(
                user=user, first_name=user.first_name, last_name=user.last_name, email=user.email)
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            page_data = {"join_form": join_form}
            return render(request, 'core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = {"join_form": join_form}
        return render(request, 'core/join.html', page_data)


def user_login(request):
    context = {"messages":"", "login_form" : LoginForm}
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    try:
                        UserProfile.objects.get(user=user)
                    except:
                        UserProfile.objects.create(user=user, first_name=user.first_name, last_name=user.last_name, email=user.email)

                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                context["messages"] = "Invalid username or password"
                return render(request, 'core/login.html', context)
    else:
        return render(request, 'core/login.html', context)


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")


def createleague(request):
    context = {"form": CreateLeagueForm, "league_name": str, "league_id": str, "leagues":[]}
    if request.method == 'POST' and 'createleague' in request.POST:
        form = CreateLeagueForm(request.POST)
        if form.is_valid():
            context["league_name"] = form.cleaned_data["league_name"]
            context["league_id"] = get_random_string(10)
            messages.success(request,
                             'League Created Successfully!')
            new_league = League(league_name = context["league_name"],league_commissioner=request.user,league_id=context["league_id"])
            new_league.save()
            users = UserProfile.objects.filter(user = request.user).all()
            for user in users:
                new_league.league_members.add(user.user)
            new_league.save()
            print(new_league.league_id)
            print(new_league.league_commissioner)
            print(new_league.league_members.all())
            print(request.user)
            new_league.save
        else:
            context["form"] = form
        leagues = League.objects.all()
        for league in leagues:
            if request.user in league.league_members.all():
                context['leagues'].append(league)
                print("True")
    elif request.method == 'GET' and 'cancel' in request.GET:
        return redirect('/')
    return render(request, "core/createleague.html", context)
def joinleague(request):
    context = {"form": JoinLeague, "leagues":[]}
    if request.method == 'POST' and 'joinleague' in request.POST:
        form = JoinLeague(request.POST)
        if form.is_valid():
            league_id = form.cleaned_data["league_id"]
            try:
                league_join = League.objects.get(league_id = league_id)
            except:
                print("League Doesnt Exist")
            league_join.save()
            if request.user in league_join.league_members.all():
                print("Member already in League")
                return render(request, "core/joinleague.html", context)
            else:
                league_join.league_members.add(request.user)
                leagues = League.objects.all()
                for league in leagues:
                    if request.user in league.league_members.all():
                        context['leagues'].append(league)
                        print("True")
                print("Member added to League")
            league_join.save()

            print(league_join.league_members.all())
            path = '/groupleague/' + str(league_join.id)
            return redirect(path)
        else:
            context["form"] = form
    elif request.method == 'GET' and 'cancel' in request.GET:
        return redirect('/')
    return render(request, "core/joinleague.html", context)
def settings(request):
    try:
        user = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user = UserProfile.objects.create(
            user=request.user, first_name=request.user.first_name, last_name=request.user.last_name, email=request.user.email)

    form = EditSettings(instance=user)
    if request.method == 'POST' and 'update' in request.POST:
        form = EditSettings(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            comments = FeedItem.objects.filter(user=request.user)
            for comment in comments:
                comment.profile_picture = user.profile_picture
                comment.save()
    context = {'form': form, "leagues": []}
    leagues = League.objects.all()
    for league in leagues:
        if request.user in league.league_members.all():
            context['leagues'].append(league)
            print("True")
    return render(request, 'core/settings.html', context)
def groupleague(request, id):
    context = {"leagues_details":[], "leagues":[]}
    league = League.objects.get(id = id)
    context["leagues_details"] = league
    leagues = League.objects.all()
    for league1 in leagues:
        if request.user in league1.league_members.all():
            context['leagues'].append(league1)
            print("True")
    return render(request, "core/groupleague.html", context)
