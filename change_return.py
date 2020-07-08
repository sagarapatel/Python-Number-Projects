#!/usr/bin/env python3
# Program ask cost of product and money given by customer and display change in denominations
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/change_return.py
# IDE PyCharm
# Python 3.8 compatible

cost = float(input("Please enter the cost of the product "))
money = float(input("Please enter money given by customer "))
change = money - cost


def compute(change, currency):
    quantity = change / currency
    remainder = change % currency
    change = remainder
    print(str(int(quantity)) + " Note(s) of {}".format(currency))
    return round(change, 2)


if change > 100:
    change = compute(change, 100)

if change > 50:
    change = compute(change, 50)

if change > 20:
    change = compute(change, 20)

if change > 10:
    change = compute(change, 10)

if change > 5:
    change = compute(change, 5)

if change > 2:
    change = compute(change, 2)

if change > 1:
    change = compute(change, 1)

if change > 0.50:
    change = compute(change, 0.50)

if change > 0.20:
    change = compute(change, 0.20)

if change > 0.10:
    change = compute(change, 0.10)

if change > 0.05:
    change = compute(change, 0.05)

print(change)