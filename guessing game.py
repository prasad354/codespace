import random

def get_user_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input <= 0:
                raise ValueError
            return user_input
        except ValueError:
            print("Please enter a positive integer.")

def main():
    # Prompt the user for the level
    level = get_user_input("Enter a positive integer for the level: ")
    
    # Generate a random integer between 1 and the level
    target_number = random.randint(1, level)
    
    while True:
        # Prompt the user to guess the number
        guess = get_user_input(f"Guess the number between 1 and {level}: ")
        
        # Check if the guess is correct
        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
