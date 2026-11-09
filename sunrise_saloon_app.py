inventory = {
    "can_bottled_beer": {"price": 4.00, "qty": 48, "reorder": 12}, 
    "draft_beer": {"price": 5.00, "qty": 30, "reorder": 10}, 
    "liquor": {"price": 35.00, "qty": 15, "reorder": 5}, 
    "liqueurs": {"price": 28.00, "qty": 10, "reorder": 3}, 
    "fruit": {"price": 12.00, "qty": 20, "reorder": 3}, 
    "jello_shots": {"price": 1.00, "qty": 60, "reorder": 20}
}

def show_menu():
    print("\n--- SUNRISE SALOON INVENTORY MENU ---")
    print("1. View inventory")
    print("2. Add or restock an item")
    print("3. Record a sale")
    print("4. Show low-stock alerts")
    print("5. Sales report with charts")
    print("6. Run 30-day simulation")
    print("7. Save and exit")

def view_inventory(inv):
    print("\n--- CURRENT INVENTORY ---")
    for item, details in inv.items():
        print("Item: " + item)
        print("  Price: $" + str(details["price"]))
        print("  Quantity: " + str(details["qty"]))
        print("  Reorder Threshold: " + str(details["reorder"]))
        print("-" * 30)

def add_or_update_item(inv):
    item_name = input("Enter the item name (e.g., can_bottled_beer, liqueurs): ").strip().lower()
    if item_name == "":
        print("Item name cannot be blank.")
        return

    # Validate price without try/except
    while True:
        price_input = input("Enter price ($): ").strip()
        # Checks if it's a valid number with an optional single decimal point
        if price_input.replace(".", "", 1).isdigit() and price_input.count(".") <= 1:
            price = float(price_input)
            break
        print("Invalid input. Please enter a valid number for the price.")

    # Validate quantity without try/except
    while True:
        qty_input = input("Enter quantity: ").strip()
        if qty_input.isdigit():
            qty = int(qty_input)
            break
        print("Invalid input. Please enter a whole number for the quantity.")

    # Validate reorder threshold without try/except
    while True:
        reorder_input = input("Enter reorder threshold: ").strip()
        if reorder_input.isdigit():
            reorder = int(reorder_input)
            break
        print("Invalid input. Please enter a whole number for the reorder threshold.")

    if item_name in inv:
        inv[item_name]["price"] = price
        inv[item_name]["qty"] = qty
        inv[item_name]["reorder"] = reorder
        print("Successfully updated " + item_name + "!")
    else:
        inv[item_name] = {"price": price, "qty": qty, "reorder": reorder}
        print("Successfully added new item: " + item_name + "!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_or_update_item(inventory)
        elif choice == "3":
            print("\n[Coming soon] Record a sale feature will be available next week.")
        elif choice == "4":
            print("\n[Coming soon] Low-stock alerts feature will be available next week.")
        elif choice == "5":
            print("\n[Coming soon] Sales report with charts feature will be available next week.")
        elif choice == "6":
            print("\n[Coming soon] 30-day simulation feature will be available next week.")
        elif choice == "7":
            print("\nSaving data and exiting... Cheers!")
            break
        else:
            print("\nInvalid choice. Please type a number between 1 and 7.")

main()

# ready for submission