def insert_coin():
    total_cents = 0
    amount_due = 50
    
    while total_cents < amount_due:
        print(f"Amount due: {amount_due - total_cents} cents")
        try:
            coin = int(input("Insert a coin (5, 10, or 25 cents): "))
            if coin in [5, 10, 25]:
                total_cents += coin
            else:
                print("Invalid coin. Please insert 5, 10, or 25 cents.")
        except ValueError:
            print("Invalid input. Please insert a valid coin.")
    
    change = total_cents - amount_due
    print(f"Change owed: {change} cents")

# Run the function
insert_coin()
