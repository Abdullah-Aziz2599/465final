from django.shortcuts import render, redirect
from scores.forms import SubmissionForm
from core.models import League, UserProfile
from django.forms import formset_factory

# Create your views here.


def form_submission(request):
    context = {'submission_form': SubmissionForm}

    if request.method == 'POST' and 'submit_form' in request.POST:
        submission_form = SubmissionForm(request.POST)
        print(submission_form)

    elif request.method == 'GET' and 'cancel' in request.GET:
        return redirect('/')

    else:
        context['submisssion_form'] = SubmissionForm

    return render(request, 'scores/form_submission.html', context)
