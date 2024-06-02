def calculate_expression():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (x y z): ").strip()
    
    # Split the input into components
    x, y, z = expression.split()
    
    # Convert x and z to integers
    x = int(x)
    z = int(z)
    
    # Perform the arithmetic operation based on the operator y
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    
    # Output the result formatted to one decimal place
    print(f"{result:.1f}")

# Run the function
calculate_expression()
