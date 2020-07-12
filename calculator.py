#!/usr/bin/env python3
# Program ask cost of product and money given by customer and display change in denominations
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
        try:
            return operators[sign](check_digit(num_one), check_digit(num_two))
        finally:
            print("Invalid input operator.")


equation = input("Enter math equation ")
print("Answer is: " + str(check_digit(equation)))
