def calculate_fuel_percentage():
    while True:
        try:
            # Prompt the user for a fraction
            fraction = input("Enter the fraction (X/Y): ").strip()
            x, y = map(int, fraction.split('/'))

            # Check if Y is not 0 and X is less than or equal to Y
            if y != 0 and x <= y:
                # Calculate the percentage of fuel
                percentage = (x / y) * 100

                # Check if the tank is essentially empty or full
                if percentage <= 1:
                    print("E")
                elif percentage >= 99:
                    print("F")
                else:
                    print(round(percentage))  # Output the percentage rounded to the nearest integer
                break
            else:
                print("Invalid fraction. Please enter again.")
        except ValueError:
            print("Invalid input format. Please enter integers separated by '/'.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please enter again.")

# Run the function
calculate_fuel_percentage()
