#!/usr/bin/env python3
# Program ask cost of product and money given by customer and display change in denominations
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/change_return.py
# IDE PyCharm
# Python 3.8 compatible

cost = float(input("Please enter the cost of the product "))
received = float(input("Please enter money given by customer "))
change = received - cost


def compute(amount, currency, type):
    quantity = amount / currency
    remainder = amount % currency
    if currency < 1:
        print(str(int(quantity)) + " {} of ${:.2f} Cent".format(type, currency))
    else:
        print(str(int(quantity)) + " {} of ${} Dollar".format(type, currency))
    return round(remainder, 2)


if change >= 100:
    change = compute(change, 100, 'Note(s)')

if change >= 50:
    change = compute(change, 50, 'Note(s)')

if change >= 20:
    change = compute(change, 20, 'Note(s)')

if change >= 10:
    change = compute(change, 10, 'Note(s)')

if change >= 5:
    change = compute(change, 5,  'Note(s)')

if change >= 2:
    change = compute(change, 2, 'Coin(s)')

if change >= 1:
    change = compute(change, 1, 'Coin(s)')

if change >= 0.50:
    change = compute(change, 0.50, 'Coin(s)')

if change >= 0.20:
    change = compute(change, 0.20, 'Coin(s)')

if change >= 0.10:
    change = compute(change, 0.10, 'Coin(s)')

if change >= 0.05:
    change = compute(change, 0.05, 'Coin(s)')

print(change)