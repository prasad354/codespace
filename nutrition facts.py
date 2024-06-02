def get_calories(fruit):
    # Dictionary mapping fruits to their calorie counts
    calories = {
        "apple": 95,
        "avocado": 234,
        "banana": 105,
        "cantaloupe": 50,
        "grapes": 62,
        "grapefruit": 52,
        "kiwi": 42,
        "lemon": 17,
        "lime": 20,
        "orange": 62,
        "peach": 59,
        "pear": 101,
        "pineapple": 50,
        "strawberry": 4,
        "watermelon": 30
    }
    
    # Convert the input fruit to lowercase
    fruit = fruit.lower()
    
    # Check if the fruit is in the dictionary and return the calories
    return calories.get(fruit, None)

def main():
    # Prompt the user for a fruit
    fruit = input("Enter a fruit: ").strip()
    
    # Get the calorie count for the fruit
    calories = get_calories(fruit)
    
    # Output the number of calories or an error message if the fruit is not found
    if calories is not None:
        print(f"Calories: {calories}")
    else:
        print("Fruit not found in the list.")

# Run the main function
main()
