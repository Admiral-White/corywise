from rest_framework import serializers

from .models import MyUUIDModel


class UUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUUIDModel
        fields = '__all__'


