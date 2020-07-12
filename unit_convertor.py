#!/usr/bin/env python3
# Program convert different units according to user input
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/calculator.py
# IDE PyCharm
# Python 3.8 compatible

unit = {
    1: {
        12: "(x-32) * 5/9",
        21: "(x * 9/5) + 32"
    },
    2: {
        12: "x * 1000"
    }
}
print("Welcome to unit conversion ")
print("Please select one of the following number")
d_one = int(input("1 for Temperature \n2 for Mass\n"))
if d_one == 1:
    print("Select temperature unit you would like to convert\n")
    d_two = int(input("1 for Celsius\n2 for Fahrenheit\n"))
elif d_one == 2:
    print("Select Mass unit you would like to convert\n")
    d_two = int(input("1 for Kilogram\n2 for Gram\n3 for Milligram\n"))
    x = input("Please Enter value to convert ")
    formula = unit[d_one][d_two]
    print(str(eval(x)))