from django import forms
from django.contrib.auth.models import User
from core.models import League, UserProfile


class SubmissionForm(forms.Form):

    CHOICES = [('away_team', 'away'), ('home_team', 'home')]

    selection = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
