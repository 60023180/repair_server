from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    board = models.CharField(max_length=225)
    branch = models.CharField(max_length=225)
    dormitory = models.CharField(max_length=10)
    Room_number = models.CharField(max_length=5)


