import json
import sys
def load_data():
    with open("db.json","r") as file:
        data = json.load(file)
    return data
data = load_data()

def save_data(data):
    with open("db.json", "w") as file:
        json.dump(data, file, indent=4)

def display_menu():
    print("Menu:")
    for dish in data["menu"]:
      print(f"ID: {dish['id']}, Name: {dish['name']}, Price: Rs.{dish['price']}, Availability: {dish['availability']}")

def add_dish():
    print("\nAdd a new dish to the menu:")
    dish_id = len(data["menu"]) + 1
    dish_name = input("Enter dish name: ")
    dish_price = float(input("Enter dish price: "))
    dish_availability = input("Is the dish available? (yes/no): ")
    new_dish = {
        "id": dish_id,
        "name": dish_name,
        "price": dish_price,
        "availability": dish_availability
    }
    data["menu"].append(new_dish)
    save_data(data)
    print(f"\nDish {dish_name} added to the menu successfully! 🎉")

def remove_dish():
    print("\nRemove a dish from the menu:")
    dish_id = int(input("Enter dish ID: "))
    for dish in data["menu"]:
        if dish["id"] == dish_id:
            data["menu"].remove(dish)
            save_data(data)
            print(f"\nDish {dish['name']} removed from the menu successfully! 🎉")
            break
        else:
            print(f"\nDish with ID {dish_id} not found in the menu!")

def update_dish():
    print("\nUpdate a dish in the menu:")
    dish_id = int(input("Enter dish ID: "))
    for dish in data["menu"]:
        if dish["id"] == dish_id:
           print(dish)
           new_availability = input("Is the dish available? (yes/no): ")
           if new_availability == 'yes' or new_availability == 'no':
            dish["availability"] = new_availability
            save_data(data)
            print(f"\nDish {dish['name']} updated successfully! 🎉")
           else:
            print("Invalid availability. yes/no only")
            return
    print(f"\n📛Dish with ID {dish_id} not found in the menu!")
   


def place_order():
    print("\n Place a new order:")
    order_id = len(data["orders"]) + 1
    cusomer_name = input("Enter customer name: ")
    order_dish_ids = input("Enter dish IDs (comma separated eg:1,2,3): ").split(",")
    order_dishes = []
    order_total = 0
    for dish_id in order_dish_ids:
        for dish in data["menu"]:
            if dish["id"] == int(dish_id) and dish["availability"] == "yes":
                print(f"\n✅ Dish {dish['name']} added to the order successfully!")
                order_dishes.append(dish)
                order_total += dish["price"]
            elif dish["id"] == int(dish_id) and dish["availability"] == "no":
                print(f"\n❌ Dish {dish['name']} is not available!")
    # new_order = {
    #   "id": order_id,
    #   "customer_name": cusomer_name,
    #   "dishes": order_dishes,
    #   "status": "recieved",
    #   "total_price": order_total
    # }
    # data["orders"].append(new_order)
    # for dish in order_dishes:
    #     dish["availability"] = "no"
    # save_data(data)
    # print(f"\nOrder #{new_order.order_id} has been placed for {new_order.customer_name}. Total price: ${new_order.total_price:.2f}")

def update_order_status():
    print("\nUpdate order status:")
    order_id = int(input("Enter order ID: "))
    new_status = input("Enter new status: (preparing/ready for pickup/delivered) ")
    if(new_status != 'preparing' and new_status != 'ready for pickup' and new_status != 'delivered'):
      print("Invalid status. preparing/ready for pickup/delivered only")
      return
    for order in data["orders"]:
        if order["id"] == order_id:
            order["status"] = new_status
            save_data(data)
            print(f"\nOrder #{order_id} updated successfully! 🎉")
            break
        else:
            print(f"\nOrder with ID {order_id} not found!")
            break

def display_orders():
    print("\nDisplay all orders:")
    for order in data["orders"]:
        print(f"Order ID: {order['id']}, Customer Name: {order['customer_name']}, Status: {order['status']}, Total Price: Rs.{order['total_price']}")
        print("Dishes:")
        for dish in order["dishes"]:
            print(f"ID: {dish['id']}, Name: {dish['name']}, Price: Rs.{dish['price']}")

def display_available_dishes():
    print("\nDisplay all available dishes:")
    input_status = input("Enter availability (yes/no): ")
    if(input_status != 'yes' and input_status != 'no'):
      print("Invalid availability. yes/no only")
      return
    for dish in data["menu"]:
      if(input_status == "yes"):
        print("Available dishes:")
        if dish["availability"] == "yes":
            print(f"✅ ID: {dish['id']}, Name: {dish['name']}, Price: Rs.{dish['price']}")
      elif(input_status == "no"):
        print("Not available dishes:")
        if dish["availability"] == "no":
            print(f"❌ ID: {dish['id']}, Name: {dish['name']}, Price: Rs.{dish['price']}")
            

def exit_program():
    user_choice = input("\nDo you want to continue? (yes/no): ")
    if(user_choice != 'yes' and user_choice != 'no'):
      print("Invalid choice. yes/no only")
      return
    if user_choice == "yes":
        return True
    else:
        print("\nThank you for using Zomato Chronicles!")
        sys.exit()


def main():
    print("Welcome to Zomato Chronicles!")
    while True:
        print("\n1. Display Menu")
        print("2. Add Dish")
        print("3. Remove Dish")
        print("4. Update Dish")
        print("5. Place Order")
        print("6. Update Order Status")
        print("7. Display Orders")
        print("8. Display Available Dishes")
        print("9. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            display_menu()
        elif choice == 2:
            add_dish()
        elif choice == 3:
            remove_dish()
        elif choice == 4:
            update_dish()
        elif choice == 5:
            place_order()
        elif choice == 6:
            update_order_status()
        elif choice == 7:
            display_orders()
        elif choice == 8:
            display_available_dishes()
        elif choice == 9:
            print("\nThank you for using Zomato Chronicles!")
            break
        else:
            print("\nInvalid choice! Try again.")
            continue
        
main()