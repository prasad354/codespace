def check_greeting():
    # Prompt the user for a greeting
    greeting = input("Please enter a greeting: ").strip().lower()
    
    # Check the conditions and output the appropriate amount
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

# Run the function
check_greeting()
