name = input("Enter your name :\t")
print(f"Hello, {name}! Let's explore some numbers together.")
#test

numbers = []
for num in range(3):
    number = int(input("plz write your favourite numbers:\t"))
    numbers.append(number)

even_odd = []
for num in numbers:
    if num % 2 == 0:
        even_odd.append((num, "even"))
    else:
        even_odd.append((num, "odd"))

print("\nLet's see the squares of your favorite numbers:")
for num in numbers:
    print(f"The square of {num} is {num ** 2} ")

total_sum = sum(numbers)
print(f"\nThe sum of your favorite numbers is: {total_sum}.")

is_prime = True
if total_sum <= 1:
    is_prime = False
else:
    for  i in range(2 , total_sum):
        if (total_sum % i) == 0:
            is_prime = False
            #break
if is_prime:
    print(f"{total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")

print("\nHere's the breakdown of whether your numbers are even or odd:")
for num, status in even_odd:
    print(f"The number {num} is {status}.")
