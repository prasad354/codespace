def camel_to_snake():
    # Prompt the user for a camel case variable name
    camel_case = input("Enter a variable name in camel case: ").strip()
    
    # Initialize an empty list to hold the snake case characters
    snake_case = []
    
    # Iterate over each character in the camel case string
    for char in camel_case:
        # If the character is uppercase, add an underscore and the lowercase version of the character
        if char.isupper():
            snake_case.append('_')
            snake_case.append(char.lower())
        else:
            # Otherwise, add the character as is
            snake_case.append(char)
    
    # Join the list into a string to form the snake case variable name
    snake_case_name = ''.join(snake_case)
    
    # Output the snake case variable name
    print(snake_case_name)

# Run the function
camel_to_snake()
