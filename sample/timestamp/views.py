from django.shortcuts import render

# Create your views here.
from .models import MyUUIDModel
from .serializers import UUIDSerializer
from rest_framework import generics


class TimeStampView(generics.RetrieveAPIView):
    # permission_classes = (permissions.AllowAny,)
    queryset = MyUUIDModel.objects.all()
    serializer_class = UUIDSerializer


