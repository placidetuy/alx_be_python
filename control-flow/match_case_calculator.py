# match_case_calculator.py

# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the operation they want to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using if-elif-else
if operation == '+':
    result = num1 + num2
    print(f"The result is {result}.")
elif operation == '-':
    result = num1 - num2
    print(f"The result is {result}.")
elif operation == '*':
    result = num1 * num2
    print(f"The result is {result}.")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result is {result}.")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")

