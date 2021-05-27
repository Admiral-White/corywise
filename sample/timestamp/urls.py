from django.urls import path

from .views import TimeStampView

urlpatterns = [

    path('get/endpoint/<int:pk>', TimeStampView.as_view()),

]
