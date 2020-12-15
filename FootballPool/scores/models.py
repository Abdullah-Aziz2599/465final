from django.db import models

# Create your models here.


class team(models.Model):
    team_name = models.CharField(max_length=255)

class winners(models.Model):
    winning_teams = models.ManyToManyField(team)
