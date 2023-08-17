from django.contrib import admin
from django.urls import path
from .views import WeatherView

urlpatterns=[
 path('weather/<str:city>/', WeatherView.as_view(), name='weather'),
]
