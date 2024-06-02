def is_valid(s):
    # Requirement 1: The plate must be between 2 and 6 characters long.
    if not (2 <= len(s) <= 6):
        return False
    
    # Requirement 2: The plate must start with at least two letters.
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    # Requirement 3: The plate can only contain letters and numbers.
    if not s.isalnum():
        return False
    
    # Requirement 4: Numbers cannot be in the middle of the plate; they must come at the end.
    # Requirement 5: The plate cannot end with the number zero.
    number_started = False
    for char in s:
        if char.isdigit():
            if char == '0' and not number_started:
                return False
            number_started = True
        elif number_started:
            return False
    
    return True

def main():
    # Prompt the user for a vanity plate
    plate = input("Enter a vanity plate: ").strip()
    
    # Output whether the plate is valid or invalid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Run the main function
main()
