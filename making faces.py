def convert(input_string):
    # Convert the input string to lowercase
    return input_string.lower()

def main():
    # Prompt the user for input
    user_input = input("Enter a string: ")
    
    # Call the convert function on the input
    result = convert(user_input)
    
    # Print the result
    print("Converted string:", result)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
