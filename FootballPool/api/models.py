from django.db import models

# Create your models here.
class Game(models.Model):
    home_team = models.CharField(max_length = 255)
    away_team = models.CharField(max_length = 255)
    away_score = models.IntegerField()
    home_score = models.IntegerField()
    current_period = models.IntegerField()
    time_remaining = models.CharField(max_length = 255)
    home_team_image = models.ImageField(null=True, blank=True)
    away_team_image = models.ImageField(null=True, blank=True)
