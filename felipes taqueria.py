def calculate_total_cost(items, menu):
    total_cost = 0
    for item in items:
        # Convert the item to titlecase
        item = item.title()
        # Check if the item is in the menu and add its price to the total cost
        if item in menu:
            total_cost += menu[item]
    return total_cost

def main():
    # Menu of entrees and their prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    print("Welcome to Felipes Taqueria!")
    print("Please enter the items you want to order (one per line):")
    
    items = []
    try:
        while True:
            item = input().strip()
            items.append(item)
            # Calculate the total cost of items entered so far
            total_cost = calculate_total_cost(items, menu)
            # Display the total cost with a dollar sign and formatted to two decimal places
            print(f"${total_cost:.2f}")
    except EOFError:
        # End of input (Ctrl-D on Unix, Ctrl-Z on Windows)
        print("Order completed. Thank you!")

# Run the main function
if __name__ == "__main__":
    main()
