from django import forms
from django.contrib.auth.models import User
from core.models import League, UserProfile
from scores.models import UserSelection


class SubmissionForm(forms.ModelForm):
    class Meta():
        model = UserSelection
        fields = ['team_selected']
