from django.contrib import admin
from .models import Repair, RepairType, Room, RoomType, RepairStatus, Dormitory
from core import models as core_models


# Register your models here.

class RepairAdmin(admin.ModelAdmin):
    list_display = [
        'repair_id',
        'name', 'board', 'dormitory',
        'room_number', 'day', 'phone_number',
        'detail_problem', 'image',
    ]


class RepairTypeAdmin(admin.ModelAdmin):
    list_display = [
        'repair_type_name',
    ]


class RoomAdmin(admin.ModelAdmin):
    list_display = [
        'room_number',
    ]


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = [
        'room_type_name',
    ]


class RepairStatusAdmin(admin.ModelAdmin):
    list_display = [
        'status_name',
    ]


class DormitoryAdmin(admin.ModelAdmin):
    list_display = [
        'dormitory_name',
    ]


admin.site.register(Repair, RepairAdmin)
admin.site.register(RepairType, RepairTypeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(RepairStatus, RepairStatusAdmin)
admin.site.register(Dormitory, DormitoryAdmin)
