from django.shortcuts import render, redirect
from feed.forms import FeedForm
from feed.models import FeedItem, Like, DisLike
from core.models import League

def home(request):
    context = {"form":FeedForm, "comment_list":[], "leagues":[]}
    comment_list = FeedItem.objects.all()
    context["comment_list"] = comment_list
    if request.method == 'POST' and 'addcomment' in request.POST:
        form = FeedForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            FeedItem(user = request.user,name = request.user,comment = comment, profile_picture = request.user.userprofile.profile_picture).save()
            leagues = League.objects.all()
            for league in leagues:
                if request.user in league.league_members.all():
                    context['leagues'].append(league)
                    print("True")
            return redirect('/feed/')
        else:
            leagues = League.objects.all()
            for league in leagues:
                if request.user in league.league_members.all():
                    context['leagues'].append(league)
                    print("True")
            context["form"] = form
    leagues = League.objects.all()
    for league in leagues:
        if request.user in league.league_members.all():
            context['leagues'].append(league)
            print("True")
    return render(request, "feed/home.html", context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        feed_item = FeedItem.objects.get(id=comment_id)
        if user in feed_item.liked.all():
            feed_item.liked.remove(user)
        else:
            feed_item.disliked.remove(user)
            feed_item.liked.add(user)
        like, created = Like.objects.get_or_create(user=request.user, comment_id = comment_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
        leagues = League.objects.all()
    for league in leagues:
        if request.user in league.league_members.all():
            context['leagues'].append(league)
            print("True")
    return redirect('/feed/')


def dis_like_post(request):
    user = request.user
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        feed_item = FeedItem.objects.get(id=comment_id)
        if user in feed_item.disliked.all():
            feed_item.disliked.remove(user)
        else:
            feed_item.liked.remove(user)
            feed_item.disliked.add(user)
        dislike, created = DisLike.objects.get_or_create(user=request.user, comment_id = comment_id)
        if not created:
            if dislike.value == 'Dislike':
                dislike.value = 'Un-dislike'
            else:
                dislike.value = 'Dislike'
        dislike.save()
    leagues = League.objects.all()
    for league in leagues:
        if request.user in league.league_members.all():
            context['leagues'].append(league)
            print("True")
    return redirect('/feed/')
