#!/usr/bin/env python3
# Program does the multiple calculations of basic math operators
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/calculator.py
# IDE PyCharm
# Python 3.8 compatible

from operator import truediv, mul, add, sub, pow, mod

# Dictionaries of different operators
operators = {
    "**": pow,
    "+": add,
    "-": sub,
    "/": truediv,
    "*": mul,
    "%": mod
}


# Function convert digit into float and operate from given dictionary
def check_digit(n):
    if n.isdigit():
        return float(n)
    for x in operators.keys():
        num_one, sign, num_two = n.partition(x)
        if sign in operators:
            return operators[sign](check_digit(num_one), check_digit(num_two))


equation = input("Enter math equation ")
print("Answer is: " + str(check_digit(equation)))
