from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.read_dish, name="home"),
    # path("add_dish/", views.add_dish, name="add_dish"),
]
