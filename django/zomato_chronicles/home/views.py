from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
DATA_BASE = {
    "menu": [
        {
            "id": 1,
            "name": "Pastaa",
            "price": 8.99,
            "available": True,
            "description": "Delicious pasta with a variety of sauces and ingredients. ",
        },
        {
            "id": 2,
            "name": "Pizza",
            "price": 10.99,
            "available": False,
            "description": "Authentic Italian pizza with a variety of toppings.",
        },
        {
            "id": 3,
            "name": "Burger",
            "price": 6.99,
            "available": True,
            "description": "Juicy burger served with crispy fries and toppings.",
        },
        {
            "id": 4,
            "name": "Salad",
            "price": 5.99,
            "available": True,
            "description": "Fresh and healthy salad with a mix of vegetables and dressings.",
        },
        {
            "id": 5,
            "name": "Steak",
            "price": 15.99,
            "available": True,
            "description": "Premium steak cooked to perfection, served with sides.",
        },
        {
            "id": 6,
            "name": "Sandwich",
            "price": 4.99,
            "available": True,
            "description": "Classic sandwich with a variety of fillings and flavors.",
        },
        {
            "id": 7,
            "name": "Soups",
            "price": 3.99,
            "available": True,
            "description": "Warm and comforting soup with a variety of ingredients",
        },
        {
            "id": 8,
            "name": "Sushi",
            "price": 12.99,
            "available": True,
            "description": "Fresh sushi rolls with a mix of seafood and flavors.",
        },
        {
            "id": 9,
            "name": "Dessert",
            "price": 7.99,
            "available": True,
            "description": "Delectable desserts ranging from cakes to ice creams.",
        },
        {
            "id": 10,
            "name": "Drinks",
            "price": 2.99,
            "available": True,
            "description": "Refreshing drinks including juices, sodas, and more.",
        },
        {
            "id": 11,
            "name": "Chicken tanduri",
            "price": 20.0,
            "available": True,
            "description": "This chicken have four legs that's why price is little bit high",
        },
    ],
    "orders": [
        {
            "id": 1,
            "customer_name": "John Doe",
            "dishes": [
                {"id": 1, "name": "Pasta", "price": 8.99},
                {"id": 3, "name": "Burger", "price": 6.99},
            ],
            "status": "received",
            "total_price": 15.98,
        },
        {
            "id": 2,
            "customer_name": "Jane Smith",
            "dishes": [
                {"id": 2, "name": "Pizzaa", "price": 10.99},
                {"id": 4, "name": "Salad", "price": 5.99},
            ],
            "status": "preparing",
            "total_price": 16.98,
        },
        {
            "id": 3,
            "customer_name": "Michael Johnson",
            "dishes": [{"id": 5, "name": "Steak", "price": 15.99}],
            "status": "ready for pickup",
            "total_price": 15.99,
        },
        {
            "id": 4,
            "customer_name": "Emily Brown",
            "dishes": [
                {"id": 1, "name": "Pasta", "price": 8.99},
                {"id": 4, "name": "Salad", "price": 5.99},
                {"id": 5, "name": "Steak", "price": 15.99},
            ],
            "status": "preparing",
            "total_price": 30.97,
        },
        {
            "id": 5,
            "customer_name": "David Wilson",
            "dishes": [
                {"id": 3, "name": "Burger", "price": 6.99},
                {"id": 5, "name": "Steak", "price": 15.99},
            ],
            "status": "delivered",
            "total_price": 22.98,
        },
        {
            "id": 6,
            "customer_name": "Hrithik vishwakarma",
            "dishes": [
                {
                    "id": 1,
                    "name": "Pasta",
                    "price": 8.99,
                    "available": True,
                    "description": "Delicious pasta with a variety of sauces and ingredients.",
                },
                {
                    "id": 2,
                    "name": "Pizzaa",
                    "price": 10.99,
                    "available": True,
                    "description": "Authentic Italian pizza with a variety of toppings.",
                },
            ],
            "status": "preparing",
            "total_price": 19.98,
        },
    ],
}


def read_dish(request):
    menu = DATA_BASE["menu"]
    return render(request, "home.html", {"menu": menu})


def update_dish(request, dish_id):
    if request.method == "POST":
        menu = DATA_BASE["menu"]
        orders = DATA_BASE["orders"]
        dish = menu[dish_id - 1]
        dish["name"] = request.POST.get("name")
        dish["price"] = request.POST.get("price")
        dish["available"] = [True if request.POST.get("available") == "on" else False][
            0
        ]
        dish["description"] = request.POST.get("description")
        DATA_BASE["menu"] = menu
        DATA_BASE["orders"] = orders
        return redirect("home")
    else:
        menu = DATA_BASE["menu"]
        dish = menu[dish_id - 1]
        return render(request, "update.html", {"dish": dish})


def add_dish(request):
    if request.method == "POST":
        menu = DATA_BASE["menu"]
        orders = DATA_BASE["orders"]

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
        DATA_BASE["menu"] = menu
        DATA_BASE["orders"] = orders
        return redirect("home")

    return render(request, "add_dish.html")

def orders(request):
    orders = DATA_BASE["orders"]
    return render(
        request,
        "orders.html",
        {"orders": orders},
    )


def update_order_status(request, order_id):
    if request.method == "POST":
        menu = DATA_BASE["menu"]
        orders = DATA_BASE["orders"]
        order = orders[order_id - 1]
        order["status"] = request.POST.get("status")
        DATA_BASE["menu"] = menu
        DATA_BASE["orders"] = orders
        return redirect("orders")
    else:
        orders = DATA_BASE["orders"]
        order = orders[order_id - 1]
        return render(
            request,
            "update_order_status.html",
            {"order": order},
        )


def place_order(request, dish_id):
    menu = DATA_BASE["menu"]
    orders = DATA_BASE["orders"]
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        selected_dishes = request.POST.getlist("selected_dishes[]")

        # Convert selected_dishes to integers
        selected_dishes = [int(dish_id) for dish_id in selected_dishes]
        # Create the order
        new_order = {
            "id": len(orders) + 1,
            "customer_name": customer_name,
            "dishes": [menu[dish_id - 1] for dish_id in selected_dishes],
            "status": "received",
            "total_price": sum(
                menu[dish_id - 1]["price"] for dish_id in selected_dishes
            ),
        }

        print(new_order)
        DATA_BASE["orders"].append(new_order)
        DATA_BASE["menu"] = menu

        return redirect("orders")

    return render(request, "place_order.html", {"current_id": dish_id, "menu": menu})


def search_dish(request):
    query = request.GET.get("search")
    menu = DATA_BASE["menu"]

    if query:
        search_results = [
            dish for dish in menu if query.lower() in dish["name"].lower()
        ]
    else:
        search_results = menu

    return render(request, "home.html", {"menu": search_results, "query": query})


def delete_dish(request, dish_id):
    menu = DATA_BASE["menu"]
    menu.pop(dish_id - 1)
    DATA_BASE["menu"] = menu
    return redirect("home")
