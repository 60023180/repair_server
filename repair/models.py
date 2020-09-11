from django.db import models
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime

import uuid


def random_repair_code():
    return uuid.uuid4().hex[:8].upper()


def random_room_code():
    return uuid.uuid4().hex[:8].upper()


def random_room_type_code():
    return uuid.uuid4().hex[:8].upper()


def random_dormitory_code():
    return uuid.uuid4().hex[:8].upper()


def random_status_code():
    return uuid.uuid4().hex[:8].upper()


# Create your models here.
class Dormitory(models.Model):
    dormitory_id = models.SlugField(unique=True, default=random_dormitory_code)
    dormitory_name = models.IntegerField(choices=[
        (1, 'UP DORM 1 (ห้องปรับอากาศ)'),
        (2, 'UP DORM 2 (ห้องพัดลม)'),
        (3, 'UP DORM 3 (ห้องพัดลม)'),
        (4, 'UP DORM 4 (ห้องพัดลม)'),
        (5, 'UP DORM 5 (ห้องพัดลม)'),
        (6, 'UP DORM 6 (ห้องพัดลม)'),
        (7, 'UP DORM 7 (ห้องพัดลม)'),
        (8, 'UP DORM 8 (ห้องพัดลม)'),
        (9, 'UP DORM 9 (ห้องพัดลม)'),
        (10, 'UP DORM 10 (ห้องปรับอากาศ)'),
        (11, 'UP DORM 11 (ห้องปรับอากาศ)'),
        (12, 'UP DORM 12 (ห้องปรับอากาศ)'),
        (13, 'UP DORM 13 (ห้องปรับอากาศ)'),
        (14, 'UP DORM 14 (ห้องพัดลม)'),
        (15, 'UP DORM 15 (ห้องพัดลม)'),
        (16, 'UP DORM 16 (ห้องพัดลม)'),
        (17, 'UP DORM 17 (ห้องพัดลม)'),
        (18, 'UP DORM 18 (ห้องพัดลม)'),
        (19, 'UP DORM 19 (ห้องพัดลม)'),
        (20, 'UP DORM 20 (ห้องพัดลม)'),
        (21, 'UP DORM 21 (ห้องพัดลม)'),
        (22, 'UP DORM 22 (ห้องพัดลม)'),
        (23, 'UP DORM 23 (ห้องพัดลม)'),
        (24, 'UP DORM 24 (ห้องพัดลม)'),
        (25, 'UP DORM 25 (ห้องปรับอากาศ)'),
        (26, 'UP DORM 26 (ห้องปรับอากาศ)'),
        (27, 'UP DORM 27 (ห้องปรับอากาศ)'),
        (28, 'UP DORM 28 (ห้องปรับอากาศ)'),
        (29, 'UP DORM 29 (ห้องปรับอากาศ)'),
        (30, 'UP DORM 30 (ห้องปรับอากาศ)'),
        (31, 'UP DORM 31 (ห้องปรับอากาศ)'),
        (32, 'UP DORM 32 (ห้องปรับอากาศ)')

    ])


class RepairType(models.Model):
    repair_type_id = models.SlugField(unique=True, default=random_room_code)
    repair_type_name = models.IntegerField(choices=[
        (1, 'ไฟฟ้า'),
        (2, 'ประปา'),
        (3, 'เฟอร์นิเจอร์'),
        (4, 'โครงสร้าง')
    ])


class Room(models.Model):
    room_id = models.SlugField(unique=True, default=random_room_code)
    room_number = models.CharField(max_length=5)


class RoomType(models.Model):
    room_id = models.SlugField(unique=True, default=random_room_type_code)
    room_type_name = models.IntegerField(choices=[
        (1, 'ห้องพัดลม,'),
        (2, 'ห้องปรับอากาศ')
    ])


class RepairStatus(models.Model):
    status_id = models.SlugField(unique=True, default=random_status_code)
    status_name = models.IntegerField(choices=[
        (1, 'แจ้งซ่อม,'),
        (2, 'กำลังดำเนินการ'),
        (3, 'ดำเนินการเสร็จสิ้น,'),
        (4, 'ยกเลิกคำขอ'),
    ])


class Repair(models.Model):
    repair_id = models.SlugField(unique=True, default=random_repair_code)
    name = models.CharField(max_length=255)
    board = models.CharField(max_length=225)
    dormitory = models.OneToOneField(Dormitory, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=225)
    day = models.DateField()
    phone_number = models.CharField(max_length=10)
    detail_problem = models.CharField(max_length=255)
    image = models.FileField(upload_to='up_image', blank=True)
