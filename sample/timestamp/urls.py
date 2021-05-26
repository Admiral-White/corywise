from django.urls import path

from .views import TimeStampView

urlpatterns = [

    path('get/endpoint', TimeStampView.as_view()),

]
