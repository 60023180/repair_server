from rest_framework import serializers
from .models import Repair, RepairType, Room, RoomType, RepairStatus, Dormitory


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = ['repair_id', 'name', 'board', 'dormitory',
                  'room_number', 'day', 'phone_number',
                  'detail_problem', 'image']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number']


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['room_type_name']


class RepairStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairStatus
        fields = ['status_name']


class RepairTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairType
        fields = ['repair_type_name']


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = ['dormitory_name']
