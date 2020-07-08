#!/usr/bin/env python3
# Program ask cost of product and money given by customer and display change in denominations
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/change_return.py
# IDE PyCharm
# Python 3.8 compatible

cost = int(input("Please enter the cost of the product "))
money = int(input("Please enter money given by customer "))
change = money - cost
if change > 100:
    hundreds = change/100
    remainder = change%100
    change = remainder
    print(str(int(hundreds)) + " Note of $100")
if change > 50:
    fifties = change/50
    remainder = change%50
    change = remainder
    print(str(int(fifties)) + " Note of $50")
if change > 20:
    twenties = change/20
    remainder = change%20
    change = remainder
    print(str(int(twenties)) + " Note of $20")