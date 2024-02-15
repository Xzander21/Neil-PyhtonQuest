def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == 'x':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error! Division by zero!"
        else:
            return num1 / num2
    else:
        return "Invalid operation!"

print("Welcome to Simple Calculator for Alf!")

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operation (+, -, x, /): ")

        result = calculate(num1, num2, operator)
        print("Result:", result)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    break