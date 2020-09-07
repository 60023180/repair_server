from django.db import models
from rest_framework import status
from rest_framework.response import Response
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

import uuid


def random_course_code():
    return uuid.uuid4().hex[:8].upper()


# def empty_view(self):
# content = {'please move along': 'nothing to see here'}
# return Response(content, status=status.HTTP_404_NOT_FOUND)
category = get_user_model()


# Create your models here.
class GetCategory(models.Model):
    category_name = models.OneToOneField(category, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Repair(models.Model):
    repair_id = models.SlugField(unique=True, default=random_course_code)
    name = models.CharField(max_length=255)
    board = models.CharField(max_length=225)
    branch = models.CharField(max_length=225)
    dormitory_number = models.CharField(max_length=10)
    Room_number = models.CharField(max_length=5)
    Phone_number = models.CharField(max_length=10)
    detail_problem = models.CharField(max_length=255)
    image = models.FileField(upload_to='up_image', blank=True)




# reImage = models.ImageField(upload_to='images/', blank=True)

# category = models.BooleanField()

# status = models.CharField(max_length=2, choices=C_STATUS)


class Roles(models.Model):
    role_id = models.SlugField(unique=True, default=random_course_code)
    role_name = models.CharField(max_length=100)
