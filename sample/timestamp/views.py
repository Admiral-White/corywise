from django.shortcuts import render

# Create your views here.
from .timestamp.models import MyUUIDModel
from sample.timestamp.serializers import UUIDSerializer
from rest_framework import generics


class TimeStampView(generics.RetrieveAPIView):
    queryset = MyUUIDModel.objects.all()
    serializer_class = UUIDSerializer


