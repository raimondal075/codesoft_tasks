

print("----- SIMPLE CALCULATOR -----")
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: ")) 
print("Choose an operation:")
print("+  for Addition")
print("-  for Subtraction")
print("*  for Multiplication")
print("/  for Division")
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = first_number + second_number
    print(f"Result: {first_number} + {second_number} = {result}")

elif operation == "-":
    result = first_number - second_number
    print(f"Result: {first_number} - {second_number} = {result}")

elif operation == "*":
    result = first_number * second_number
    print(f"Result: {first_number} * {second_number} = {result}")

elif operation == "/":
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = first_number / second_number
        print(f"Result: {first_number} / {second_number} = {result}")

else:
    print("Invalid operation. Please enter one of +, -, *, /.")