from django.urls import path
from . import views
urlpatterns = [
    path('menu/', views.get_menu_items_api, name='menu_list'),
    path('menu/create/', views.create_menu_item, name='create_menu_item'),
]