#!/usr/bin/env python3
# Program ask cost of product and money given by customer and display change in denominations
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/calculator.py
# IDE PyCharm
# Python 3.8 compatible

from operator import truediv, mul, add, sub

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv
}

equation = input("Enter math equation ")


def check_digit(n):
    if n.isdigit():
        return float(n)
    for x in operators.keys():
        num_one, sign, num_two = n.partition(x)
        if sign in operators:
            print(num_one, sign, num_two)
            return operators[sign](check_digit(num_one), check_digit(num_two))


print(str(check_digit(equation)))
