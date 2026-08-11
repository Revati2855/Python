inventory = {}

def add_product():
    name = input("Enter product name: ")
    qty = int(input("Enter quantity: "))
    inventory[name] = qty
    print("Product added successfully!\n")

def update_product():
    name = input("Enter product name: ")

    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty

        if inventory[name] == 0:
            del inventory[name]
            print("Product sold out and removed from inventory!\n")
        else:
            print("Quantity updated successfully!\n")
    else:
        print("Product not found!\n")

def highest_stock():
    if len(inventory) == 0:
        print("Inventory is empty!\n")
    else:
        product = max(inventory, key=inventory.get)
        print("Product with Highest Stock:", product)
        print("Quantity:", inventory[product], "\n")

def display_inventory():
    if len(inventory) == 0:
        print("Inventory is empty!\n")
    else:
        print("\nInventory:")
        for product, qty in inventory.items():
            print(product, ":", qty)
        print("Total Unique Products:", len(inventory))
        print()

while True:
    print("----- Inventory Management System -----")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Display Highest Stock")
    print("4. Display Inventory")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_product()
    elif choice == 2:
        update_product()
    elif choice == 3:
        highest_stock()
    elif choice == 4:
        display_inventory()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice!\n")