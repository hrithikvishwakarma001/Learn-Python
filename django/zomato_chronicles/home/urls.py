from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.read_dish, name="home"),
    path("add_dish/", views.add_dish, name="add_dish"),
    path("update_dish/<int:dish_id>/", views.update_dish, name="update_dish"),
    path("orders/", views.orders, name="orders"),
    path(
        "update_order_status/<int:order_id>/",
        views.update_order_status,
        name="update_order_status",
    ),
]
