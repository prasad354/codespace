import random

def generate_problem():
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    return x, y, x + y

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("Please enter a valid non-negative integer.")

def main():
    score = 0
    
    # Prompt the user for the level
    while True:
        level = input("Enter the level (1, 2, or 3): ")
        if level in ["1", "2", "3"]:
            level = int(level)
            break
        print("Please enter 1, 2, or 3.")
    
    print(f"Level {level}: You have 3 tries for each problem.")
    
    # Generate and solve 10 math problems
    for _ in range(10):
        x, y, answer = generate_problem()
        print(f"\n{level}. {x} + {y} = ")
        
        for attempt in range(3):
            user_answer = get_user_input("Your answer: ")
            if user_answer == answer:
                print("Correct!")
                score += 1
                break
            else:
                print("EEE. Please try again.")
        
        if user_answer != answer:
            print(f"Sorry, the correct answer is {answer}.")
        
        level += 1
    
    print(f"\nYour score: {score} out of 10.")

if __name__ == "__main__":
    main()
