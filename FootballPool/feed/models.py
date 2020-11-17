from django.db import models

# Create your models here.
class FeedItem(models.Model):
    comment = models.CharField(max_length = 255);
