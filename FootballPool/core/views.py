from django.shortcuts import render, redirect
from core.forms import JoinForm, LoginForm, CreateLeagueForm, JoinLeague
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.models import UserProfile
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


@login_required(login_url='/login/')
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")


def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            user = join_form.save()
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
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
        return render(request, 'core/login.html', {"login_form": LoginForm})


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")
def createleague(request):
    context = {"form":CreateLeagueForm}
    if request.method == 'POST' and 'createleague' in request.POST:
        form = CreateLeagueForm(request.POST)
        if form.is_valid():
            league_name = form.cleaned_data["league_name"]
            league_password = form.cleaned_data["league_password"]
            return redirect('/')
        else:
            context["form"] = form
    elif request.method =='GET' and 'cancel' in request.GET:
        return redirect('/')
    return render(request, "core/createleague.html", context)
def joinleague(request):
    context = {"form":JoinLeague}
    if request.method == 'POST' and 'joinleague' in request.POST:
        form = JoinLeague(request.POST)
        if form.is_valid():
            league_id = form.cleaned_data["league_id"]
            league_password = form.cleaned_data["league_password"]
            return redirect('/')
        else:
            context["form"] = form
    elif request.method =='GET' and 'cancel' in request.GET:
        return redirect('/')
    return render(request, "core/joinleague.html", context)
