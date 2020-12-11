from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# from django.utils.crypto import get_random_string >>> this needs to go into groups


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(
        default="yoda.png", null=True, blank=True)


class League(models.Model):  # unique league
    league_name = models.CharField(max_length=30)
    league_id = models.CharField(max_length=10)
    league_commissioner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commissioner")  # only 1 user
    league_members = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="members")

    # def __str__(self):
    # return self.league_id
