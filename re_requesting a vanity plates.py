import re

def main():
    plate = input("Enter a vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the plate consists of only uppercase letters, digits, or dashes
    if not re.match(r'^[A-Z0-9-]+$', s):
        return False

    # Check if the plate contains exactly 7 characters
    if len(s) != 7:
        return False

    # Check if the plate has 3 digits
    if not re.match(r'.*\d.*\d.*\d.*', s):
        return False

    # Check if the plate has 4 letters
    if not re.match(r'.*[A-Z].*[A-Z].*[A-Z].*[A-Z].*', s):
        return False

    return True

if __name__ == "__main__":
    main()
