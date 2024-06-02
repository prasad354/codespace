import sys
import csv
from tabulate import tabulate

def load_pizzas(filename):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            pizzas = [row for row in reader]
            return pizzas
    except FileNotFoundError:
        sys.exit("File not found.")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <filename.csv>")
    
    filename = sys.argv[1]
    
    # Check if the file name ends with .csv
    if not filename.endswith(".csv"):
        sys.exit("File must have a .csv extension.")

    pizzas = load_pizzas(filename)
    print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
