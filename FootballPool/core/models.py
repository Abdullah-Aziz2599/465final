from django.db import models

# Create your models here.


class Login(models.Model){
    name = CharField(max_length = 250)
}
