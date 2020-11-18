from django.db import models

# Create your models here.
class FeedItem(models.Model):
    name = models.CharField(max_length = 255)
    comment = models.CharField(max_length = 255)
    date = models.DateTimeField(auto_now_add = True)
    like = models.BooleanField(default = False)
