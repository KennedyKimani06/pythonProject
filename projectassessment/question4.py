# Simple Calculator with Conditionals

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and print the result
if operation == '+':
    print(f"Result: {num1 + num2}")
elif operation == '-':
    print(f"Result: {num1 - num2}")
elif operation == '*':
    print(f"Result: {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")
