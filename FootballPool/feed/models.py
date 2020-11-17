from django.db import models

# Create your models here.
class FeedItem(models.Model):
    comment = CharField(max_length = 255);
