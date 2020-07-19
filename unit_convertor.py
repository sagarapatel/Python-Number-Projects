#!/usr/bin/env python3
# Program convert different units according to user input
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/calculator.py
# IDE PyCharm
# Python 3.8 compatible

# Dict[int, Dict[int, Tuple[str, str]]]
unit = {
    0: {
        1: "Temperature", 2: "Mass", 3: "Currency", 4: "Volume", 5: "Distance"
    },
    1: {
        1: "Celsius", 2: "Fahrenheit",
        12: "(x * 9/5) + 32", 21: "(x-32) * 5/9"
    },
    2: {
        1: "Kilogram", 2: "Gram", 3: "Milligram",
        12: "x * 1000", 13: "x * 1000000", 21: "x / 1000", 23: "x * 1000", 31: "x / 1000000", 32: "x / 1000"
    },
    3: {
        1: "USD", 2: "EUR", 3: "GBP", 4: "INR", 5: "CAD", 6: "AUD", 7: "SGD",
        12: "x*0.87516", 13: "x*0.79566", 14: "x*74.9067", 15: "x*1.35756", 16: "x*1.42939", 17: "x*1.39006",
        21: "x*1.14265", 23: "x*0.90916", 24: "x*85.5921", 25: "x*1.55122", 26: "x*1.63329", 27: "x*1.58835",
        31: "x*1.25683", 32: "x*1.09992", 34: "x*94.1446", 35: "x*1.70622", 36: "x*1.79649", 37: "x*1.74706",
        41: "x*0.01335", 42: "x*0.01168", 43: "x*0.01062", 45: "x*0.01812", 46: "x*0.01908", 47: "x*0.01856",
        51: "x*0.73661", 52: "x*0.64465", 53: "x*0.58609", 54: "x*55.1772", 56: "x*1.05291", 57: "x*1.02394",
        61: "x*1.42939", 62: "x*1.63329", 63: "x*0.55664", 64: "x*52.4047", 65: "x*0.94975", 67: "x*0.97248",
        71: "x*0.71939", 72: "x*0.62958", 73: "x*0.57239", 74: "x*53.8874", 75: "x*0.97662", 76: "x*1.02829"
    },
    4: {
        1: "Centiliter", 2: "Milliliter", 3: "Liter",
        12: "x * 10", 13: "x / 100", 21: "x / 10", 23: "x / 1000", 31: "x * 100", 32: "x * 1000"
    },
    5: {
        1: "Inch", 2: "Centimeter", 3: "Meter", 4: "Kilometer",
        12: "x * 2.54", 13: "x / 39.37", 14: "x / 39370 ", 21: "x / 2.54", 23: "x / 100", 24: "x / 100000",
        31: "x * 39.3701", 32: "x * 100", 34: "x / 1000", 41: "x * 39370", 42: "x * 100000", 43: "x * 1000"
    }
}


# Function which merge the selected numbers to get right formula
def selection(num_one, num_two):
    merge_sel = int(str(num_one) + str(num_two))
    return merge_sel


# Display options to select from
def options(dic_value, sel_value):
    for x in dic_value:
        if x < 12 and x != sel_value:
            print("Enter " + str(x) + " for " + dic_value[x])


print("Welcome to unit conversion ")
print("Please select one of the Conversions")
options((unit[0]), 0)  # Display main unit conversions to select from
d_one = int(input())

print("\nSelect {} unit to convert FROM ".format(unit[0][d_one]))
options(unit[d_one], 0)  # Display option one to convert unit from
sel_one = int(input())  # Select option one

print("\nSelect {} unit to convert TO ".format(unit[0][d_one]))
options(unit[d_one], sel_one)  # Display option two to convert unit to
sel_two = int(input())  # Select option two

d_two = selection(sel_one, sel_two)

x = int(input("\nPlease Enter value to convert {} to {} ".format(unit[d_one][sel_one], unit[d_one][sel_two])))
# Select formula according to options selected
formula = unit[d_one][d_two]
print(str(x) + " " + unit[d_one][sel_one] + " = " + str(round(eval(formula), 2)) + " " + unit[d_one][sel_two])
