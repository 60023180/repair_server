from repair import models, serializers
from rest_framework import viewsets
from repair.models import Repair, RepairType, Room, RoomType, RepairStatus, Dormitory


# Create your views here.
class RepairViewSet(viewsets.ModelViewSet):
    queryset = models.Repair.objects.all()
    serializer_class = serializers.RepairSerializer


class RepairTypeViewSet(viewsets.ModelViewSet):
    queryset = models.RepairType.objects.all()
    serializer_class = serializers.RepairTypeSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = models.RoomType.objects.all()
    serializer_class = serializers.RoomTypeSerializer


class RepairStatusViewSet(viewsets.ModelViewSet):
    queryset = models.RepairStatus.objects.all()
    serializer_class = serializers.RepairStatusSerializer


class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = models.Dormitory.objects.all()
    serializer_class = serializers.DormitorySerializer
