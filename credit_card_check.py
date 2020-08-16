#!/usr/bin/env python3
# Program ask cost of product and money given by customer and display change in denominations
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/credit_card_check.py
# IDE PyCharm
# Python 3.8 compatible

import sys


# Check credit card number Luhn algorithm
def luhn(n):
    try:
        r = [int(ch) for ch in str(n)][::-1]
        return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0
    except ValueError:
        print("Only digits excepted for check.")
        sys.exit(0)


card_number = input("Please enter credit card number to check ")
print(luhn(card_number))
