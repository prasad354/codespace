import sys

def main():
    # Check if the number of Bitcoins argument is provided
    if len(sys.argv) != 2:
        print("Usage: python program_name.py <number_of_bitcoins>")
        sys.exit(1)
    
    # Try to convert the argument to a float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: The number of Bitcoins must be a valid number.")
        sys.exit(1)
    
    # Continue with the program logic here
    print(f"Number of Bitcoins to buy: {bitcoins}")

if __name__ == "__main__":
    main()
