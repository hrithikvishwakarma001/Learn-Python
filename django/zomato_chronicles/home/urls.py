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
    path('place_order/<int:dish_id>/', views.place_order, name='place_order'),
    path('search_dish/', views.search_dish, name='search_dish'),
    path('delete_dish/<int:dish_id>/', views.delete_dish, name='delete_dish'),
]
