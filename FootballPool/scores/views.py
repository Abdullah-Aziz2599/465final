from django.shortcuts import render, redirect
from scores.forms import SubmissionForm
from core.models import League, UserProfile
from django.forms import formset_factory

# Create your views here.


def form_submission(request):
    formset = formset_factory(SubmissionForm, extra=2)
    formset = SubmissionForm(initial=[
        {'away_team': 'away team', 'home_team': 'Home Team'}
    ])

    return (request, 'form_submission.html')
