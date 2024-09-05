def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

num1 = int(input("Write any number: "))
operation = input("Please add the operation (+, -, *, /): ")
num2 = int(input("Write any number: "))

if operation == "+":
    print(f"The sum of your numbers is {add(num1, num2)}")
elif operation == "-":
    print(f"The difference of your numbers is {subtract(num1, num2)}")
elif operation == "*":
    print(f"The product of your numbers is {multiply(num1, num2)}")
elif operation == "/":
    print(f"The quotient of your numbers is {divide(num1, num2)}")
else:
    print("Invalid operation!")
