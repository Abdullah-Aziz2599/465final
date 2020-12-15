from django import forms
from django.contrib.auth.models import User
from core.models import League, UserProfile


class SubmissionForm(forms.Form):
    away_team = forms.BooleanField()
    home_team = forms.BooleanField()
