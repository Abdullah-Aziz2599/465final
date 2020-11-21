from django import forms
from django.contrib.auth.models import User
from core.models import League


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
        fields = ['league_name', 'league_password']


class JoinLeague(forms.ModelForm):
    class Meta():
        model = League
        fields = ['league_id', 'league_password']
