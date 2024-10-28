from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)




