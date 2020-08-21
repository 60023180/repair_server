from repair import models
from rest_framework import serializers


class TeachingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Category


class RepairSerializer(serializers.ModelSerializer):
    teaching_period = TeachingPeriodSerializer()

    class Meta:
        fields = '__all__'
        model = models.Repair

    def create(self, validated_data):
        teaching_period = validated_data.pop('teaching_period')
        teaching_period = models.Category.objects.create(**teaching_period)
        repair = models.Repair.objects.create(teaching_period=teaching_period, **validated_data)
        return repair

    def update(self, instance, validated_data):
        teaching_period_data = validated_data.pop('teaching_period')
        teaching_period = instance.teaching_period

        instance.name = validated_data.get('name', instance.name)
        instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        teaching_period.start_time = teaching_period_data.get('start_time', teaching_period.start_time)
        teaching_period.end_time = teaching_period_data.get('end_time', teaching_period.end_time)
        teaching_period.day = teaching_period_data.get('day', teaching_period.day)
        teaching_period.save()

        return instance
