#!/usr/bin/env python3
# Find PI to the Nth Digit
# Program generate PI with decimal places up to value of n
# Limit upto 10000 decimal places of PI.
# Github: https://github.com/sagarapatel/Python-Number-Projects/blob/master/Find_pi.py
# IDE: PyCharm
# Version: Python 3.5 compatible

import math
import decimal
from decimal import Decimal

#Function for calculating and returning pi value
def compute_pi(n):
    decimal.getcontext().prec = n + 1
    pi = Decimal(0)

    for k in range(n):
        pi += Decimal(math.pow(16, -k)) * (Decimal(4 / (8 * k + 1)) - Decimal(2 / (8 * k + 4)) -
                                           Decimal(1 / (8 * k + 5)) - Decimal(1 / (8 * k + 6)))
    return pi

#Exceptions to check and handle Errors and out of range input.
while True:
    try:
        value = input("Enter Decimal places you want for pi between 1 and 10000 ")
        n = int(value)
        if n in range(1, 10000):
            print("Value of pi with "+ str(n) +" decimals is " + str(compute_pi(n)))
        else:
            response = input("Invalid Input. Would you like to Try Again.... (y/n) ")
            if response == 'y' or response == 'Y':
                continue
            else:
                break
    except ValueError:
        response = input("Invalid Input. Would you like to Exit.... (y/n) ")
        if response == 'y' or response == 'Y':
            break
        else:
            continue