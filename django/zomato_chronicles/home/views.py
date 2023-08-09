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
        dish["available"] = [True if request.POST.get("available") == "on" else False][
            0
        ]
        dish["description"] = request.POST.get("description")
        write_data(menu, orders)
        return redirect("home")
    else:
        menu = get_menu()
        dish = menu[dish_id - 1]
        return render(request, "update.html", {"dish": dish})


def add_dish(request):
    if request.method == "POST":
        menu, orders = read_data()

        new_dish = {
            "id": len(menu) + 1,  # Generate a new ID
            "name": request.POST.get("name"),
            "price": float(request.POST.get("price")),
            "available": False,
            "description": request.POST.get("description"),
        }
        #   print(new_dish)
        if new_dish["name"] == "":
            return HttpResponse("Name cannot be empty")
        if new_dish["price"] == "":
            return HttpResponse("Price cannot be empty")
        if new_dish["description"] == "":
            return HttpResponse("Description cannot be empty")

        menu.append(new_dish)
        write_data(menu, orders)
        return redirect("home")

    return render(request, "add_dish.html")


def orders(request):
    _, orders = read_data()
    return render(
        request,
        "orders.html",
        {"orders": orders},
    )


def update_order_status(request, order_id):
    if request.method == "POST":
        menu, orders = read_data()
        order = orders[order_id - 1]
        order["status"] = request.POST.get("status")
        write_data(menu, orders)
        return redirect("orders")
    else:
        menu, orders = read_data()
        order = orders[order_id - 1]
        return render(
            request,
            "update_order_status.html",
            {"order": order},
        )


def place_order(request, dish_id):
    menu, orders = read_data()
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        selected_dishes = request.POST.getlist("selected_dishes[]")
        # Create the order
        new_order = {
            "id": len(orders) + 1,
            "customer_name": customer_name,
            "dishes": [menu[int(dish_id) - 1] for dish_id in selected_dishes],
            "status": "received",
            "total_price": sum(
                menu[int(dish_id) - 1]["price"] for dish_id in selected_dishes
            ),
        }
        # change the available status of the in the menu dishes to False if the dish is in the order
        # for dish in menu:
        #     if dish.id in selected_dishes:
        #         dish["available"] = False

        print(new_order)
        orders.append(new_order)
        write_data(menu, orders)
        return redirect("orders")

    return render(request, "place_order.html", {"current_id": dish_id, "menu": menu})


def search_dish(request):
    query = request.GET.get("search")
    menu, _ = read_data()

    if query:
        search_results = [
            dish for dish in menu if query.lower() in dish["name"].lower()
        ]
    else:
        search_results = menu

    return render(request, "home.html", {"menu": search_results, "query": query})
