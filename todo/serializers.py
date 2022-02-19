from rest_framework import serializers

from todo.models import Todolist


class TodolistSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000, default='')
    color = serializers.CharField(max_length=255, default='Red')
    priority = serializers.IntegerField(default=3)
    time_create = serializers.TimeField(read_only=True)
    time_update = serializers.TimeField(read_only=True)
    is_pyblished = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Todolist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.color = validated_data.get("color", instance.color)
        instance.priority = validated_data.get("priority", instance.priority)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.save()
        return instance