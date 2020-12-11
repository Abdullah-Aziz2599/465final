from django import forms
from django.contrib.auth.models import User
from core.models import League, UserProfile


class JoinForm(forms.ModelForm):
    username = forms.CharField(help_text=False)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password'}))

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateLeagueForm(forms.ModelForm):
    class Meta():
        model = League
        fields = ['league_name']


class JoinLeague(forms.ModelForm):
    class Meta():
        model = League
        fields = ['league_id']


class EditSettings(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'profile_picture']
