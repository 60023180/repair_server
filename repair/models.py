from django.db import models
# from rest_framework import status
# from rest_framework.response import Response
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
    Phone_number = models.CharField(max_length=10)
    teaching_period = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail_name = models.CharField(max_length=255)
    # reImage = models.ImageField(upload_to='images/', blank=True)

    # category = models.BooleanField()

    # status = models.CharField(max_length=2, choices=C_STATUS)
