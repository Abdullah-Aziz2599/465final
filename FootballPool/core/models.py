from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# from django.utils.crypto import get_random_string >>> this needs to go into groups


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class League(models.Model):  # unique league
    league_name = models.CharField(max_length=30)
    league_id = models.CharField(max_length=10)
    league_password = models.CharField(max_length=20)
    league_commissioner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commissioner")  # only 1 user
    league_members = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="members")
