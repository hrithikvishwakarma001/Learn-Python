from django.shortcuts import render, redirect
from .db_utils import read_data, write_data
from django.http import HttpResponse

# Create your views here.


def get_menu():
    menu, _ = read_data()
    return menu


def read_dish(request):
    menu = get_menu()
    return render(request, "home.html", {"menu": menu})


def update_dish(request, dish_id):
    if request.method == "POST":
        menu, orders = read_data()
        dish = menu[dish_id - 1]  
        dish["name"] = request.POST.get("name")
        dish["price"] = request.POST.get("price")
        dish["available"] = [True if request.POST.get("available") == "on" else False][0]
        write_data(menu, orders) 
        return redirect("home") 
    else:
        menu = get_menu()
        dish = menu[dish_id - 1] 
        return render(request, "update.html", {"dish": dish})

