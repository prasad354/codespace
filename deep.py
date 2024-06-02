def check_answer():
    # Prompt the user for an answer
    user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    
    # List of acceptable answers
    valid_answers = ["42", "forty-two", "forty two"]
    
    # Check if the user input is in the list of valid answers
    if user_input in valid_answers:
        print("Yes")
    else:
        print("N")

# Run the function
check_answer()
