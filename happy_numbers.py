#!/usr/bin/env python3
# Program find if a number is happy number.
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/happy_numbers.py
# IDE PyCharm
# Python 3.8 compatible

def pdi_function(number, base: int = 10):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total = total + pow(number % base, 2)
        number = number // base
    return total


def is_happy(number: int) -> bool:
    """Determine if the specified number is a happy number."""
    while number != 1 and number != 4:
        number = pdi_function(number)
    return number == 1


x = int(input("Enter number to check if the number is a HAPPY Number "))
print(is_happy(x))
