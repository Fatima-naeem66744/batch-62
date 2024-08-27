
value1 = int(input("Plz write a number:"))
operation = input("plz enter the operation you want to perform :")
if operation not in ["+", "-", "*", "/", "//"]:
    print("Invalid operation\nOnly enters addition,subtraction multiplication or division operator")       
    
value2 = int(input("Plz write a number :"))

if operation == "+":
    print(value1 + value2)
elif operation == "-":
    print(value1-value2)
elif operation == "/":
    print(value1/value2)
elif operation == "*" :
    print(value1*value2)
elif operation == "//" :
        print(value1//value2)