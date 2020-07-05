#!/usr/bin/env python3
# Find total cost of the tiles for the given measurements and price of tiles
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/tile_cost.py
# IDE PyCharm
# Python 3.5 compatible


# Calculates the cost of tiles through area given by user.
while True:
    try:
        height = int(input("Please enter length of the area in feet "))
        width = int(input("Please enter width of the area in feet "))
        cost = int(input("Please enter cost of tiles per sq feet "))
        sq_feet = height * width
        cost = sq_feet * cost
        print("$" + str(cost) + " will be total cost of the tiles")
        break
    except ValueError:
        print("Please Enter1 correct value. Try Again.")
        continue