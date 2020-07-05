#!/usr/bin/env python3
# Calculates repayments of fixed term mortgage at given interest rates
# Calculates how user want to pay (Monthly,  Fortnightly, Weekly)
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/mortgage_calculator.py
# IDE PyCharm
# Python 3.5 compatible

from math import pow

print("Welcome to the Mortgage Calculator ")
amount = int(input("Enter the amount of Mortgage "))
interest = float(input("Enter mortgage interest rate "))
years = int(input("Enter mortgage years "))
repayments = input("Enter 'm' for Monthly repayments, 'f' for fortnightly repayments ")
if repayments == 'm' or repayments == 'M':
    interest_rate = (interest / 12) / 100
    time = years * 12
    n = 'Monthly'
elif repayments == 'f' or repayments == 'F':
    interest_rate = (interest / 26) / 100
    time = years * 26
    n = 'Fortnightly'

loan_payment = amount * ((interest_rate * pow((1 + interest_rate), time)) / (pow((1 + interest_rate), time) - 1))
print("Your {first} loan payment will be ${payment}".format(first=n, payment=round(loan_payment, 2)))
