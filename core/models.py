from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth import get_user_model
import uuid


def random_roles_code():
    return uuid.uuid4().hex[:8].upper()


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    board = models.CharField(max_length=225)
    branch = models.CharField(max_length=225)
    dormitory_number = models.CharField(max_length=10)
    Room_number = models.CharField(max_length=5)


class Permission(models.Model):
    per_name = models.CharField(max_length=225)


class Roles(models.Model):
    role_id = models.SlugField(unique=True, default=random_roles_code)
    role_name = models.CharField(max_length=100)
