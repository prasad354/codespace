def remove_vowels():
    # Prompt the user for a string of text
    text = input("Enter a string of text: ").strip()
    
    # Define the vowels to remove
    vowels = "aeiouAEIOU"
    
    # Create a new string with vowels removed
    result = ''.join([char for char in text if char not in vowels])
    
    # Output the result
    print(result)

# Run the function
remove_vowels()
