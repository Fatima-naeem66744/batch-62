def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while True:
    try:
        num1 = int(input("Write any number: "))
        num2 = int(input("Write another number: "))
        
        while True:  # loop until a correct operation is entered
            operation = input("Please add the operation (+, -, *, /): ")
            
            if operation == "+":
                print(f"The sum of your numbers is {add(num1, num2)}")
                break  # exit the inner loop if the operation is valid
            elif operation == "-":
                print(f"The difference of your numbers is {subtract(num1, num2)}")
                break
            elif operation == "*":
                print(f"The product of your numbers is {multiply(num1, num2)}")
                break
            elif operation == "/":
                if num2 == 0:
                    print("Cannot divide by zero, please enter a valid number.")
                    num2 = int(input("Write another number: "))  # get a new valid number
                else:
                    print(f"The quotient of your numbers is {divide(num1, num2)}")
                    break
            else:
                print("Please enter the correct operation (+, -, *, /).")
        
        break  # exit the outer loop after everything is correct

    except ValueError:
        print("Please enter valid numbers.")
