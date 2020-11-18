from django.shortcuts import render
from feed.forms import FeedForm
from feed.models import FeedItem

# Create your views here.
def home(request):
    context = {"form":FeedForm, "comment_list":[]}
    comment_list = FeedItem.objects.all()
    context["comment_list"] = comment_list
    if request.method == 'POST' and 'addcomment' in request.POST:
        form = FeedForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            FeedItem(name = request.user,comment = comment).save()
        else:
            context["form"] = form
    return render(request, "feed/home.html", context)
