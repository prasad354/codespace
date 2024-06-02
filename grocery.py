def generate_grocery_list(items):
    # Convert items to uppercase and count occurrences
    grocery_dict = {}
    for item in items:
        item = item.strip().lower()  # Convert to lowercase and remove leading/trailing whitespace
        grocery_dict[item] = grocery_dict.get(item, 0) + 1
    
    # Sort the grocery list alphabetically
    sorted_items = sorted(grocery_dict.items())
    
    # Format and return the grocery list
    grocery_list = []
    for item, count in sorted_items:
        grocery_list.append(f"{count} {item.upper()}")
    return grocery_list

def main():
    print("Welcome! Please enter your grocery list (one item per line):")
    
    items = []
    try:
        while True:
            item = input().strip()
            items.append(item)
    except EOFError:
        # End of input (Ctrl-D on Unix, Ctrl-Z on Windows)
        pass
    
    # Generate and output the grocery list
    grocery_list = generate_grocery_list(items)
    for item in grocery_list:
        print(item)

# Run the main function
if __name__ == "__main__":
    main()
