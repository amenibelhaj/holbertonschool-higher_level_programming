#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10 if number >= 0 else -(abs(number) % 10) #just a reminder by me: The abs() function is used specifically to handle negative numbers 
in a way that ensures the correct calculation of the last digit

print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
