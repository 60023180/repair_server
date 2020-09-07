from repair import models
from rest_framework import serializers


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Repair

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance
