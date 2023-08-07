
import json

def load_data():
  with open('db.json', 'r') as f:
      data = json.load(f)
  return data

data = load_data()

def display_inventory():
  for snack in data['inventory']:
      print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Availability: {snack['availability']}")

def add_snack():
  snack_name = input("Enter the name of the snack: ")
  snack_price = int(input("Enter the price of the snack: "))
  snack_availability = input("Enter the availability of the snack: ")

  snack_id = data['inventory'][-1]['id'] + 1
  new_snack = {
      "id": snack_id,
      "name": snack_name,
      "price": snack_price,
      "availability": snack_availability
  }

  data['inventory'].append(new_snack)
  save_data(data)
  print("Snack added successfully! 🎉")

def remove_snack():
  id_to_remove = int(input("Enter the ID of the snack to remove: "))
  
  for snack in data['inventory']:
      if snack['id'] == id_to_remove:
          data['inventory'].remove(snack)
          save_data(data)
          print("Snack removed from inventory.✅")
          return
  
  print("Snack not found in inventory.")

def update_availability():
  id_to_update = int(input("Enter the ID of the snack to update: "))
  
  for snack in data['inventory']:
      if snack['id'] == id_to_update:
          new_availability = input("Enter new availability (yes/no): ")
          if new_availability != 'yes' and new_availability != 'no':
              print("Invalid availability.")
              return
          snack['availability'] = new_availability
          save_data(data)
          print("Availability updated.✅")
          return
  
  print("Snack not found in inventory.")

def record_sale():
    id_sold = int(input("Enter the ID of the snack sold: "))

    for snack in data['inventory']:
        if snack['id'] == id_sold and snack['availability'] == "yes":
            data['sales'].append(snack)
            snack['availability'] = "no"
            save_data(data)
            print("Sale recorded and inventory updated.✅")
            return
        elif snack['id'] == id_sold and snack['availability'] == "no":
            print("This snack is not available for sale.")
            return
    
    print("Snack not found in inventory.")

def save_data(data):
    with open('canteen_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def main():
    while True:
        print("\nCanteen System Menu:")
        print("1. Display Inventory")
        print("2. Add Snack to Inventory")
        print("3. Remove Snack from Inventory")
        print("4. Update Snack Availability")
        print("5. Record Sale")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_snack()
        elif choice == '3':
            remove_snack()
        elif choice == '4':
            update_availability()
        elif choice == '5':
            record_sale()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
