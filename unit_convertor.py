#!/usr/bin/env python3
# Program convert different units according to user input
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/calculator.py
# IDE PyCharm
# Python 3.8 compatible

# Dict[int, Dict[int, Tuple[str, str]]]
unit = {
    0: {
        1: ("", "Temprature"),
        2: ("", "Mass")
    },
    1: {
        12: ("(x * 9/5) + 32", "Celsius"),
        21: ("(x-32) * 5/9", "Ferenheit")
    },
    2: {
        12: ("x * 1000", "Kilogram"),
        21: ("x / 1000", "Gram")
    }
}


# Function which merge and reverse the selected numbers to get right formula
def selection(num_one, num_two):
    merge_sel = int(str(num_one) + str(num_two))
    reverse_sel = int(str(merge_sel)[::-1])
    return merge_sel, reverse_sel


# Display options to select from
def options(dic_value):
    cnt = 1
    for x in dic_value:
        print("Enter " + str(cnt) + " for " + dic_value[x][1])
        cnt += 1


print("Welcome to unit conversion ")
print("Please select one of the Conversions")
options((unit[0]))  # Display main unit conversions to select from
d_one = int(input())

print("\nSelect {} unit to convert FROM ".format(unit[0][d_one][1]))
options(unit[d_one])  # Display option one to convert unit from
sel_one = int(input())  # Select option one

print("\nSelect {} unit to convert TO ".format(unit[0][d_one][1]))
options(unit[d_one])  # Display option two to convert unit to
sel_two = int(input())  # Select option two

d_two, d_two_rev = selection(sel_one, sel_two)

x = int(input("\nPlease Enter value to convert {} to {} ".format(unit[d_one][d_two][1], unit[d_one][d_two_rev][1])))
# Select formula according to options selected
formula = unit[d_one][d_two][0]
print(str(x) + " " + unit[d_one][d_two][1] + " = " + str(round(eval(formula), 2)) + " " + unit[d_one][d_two_rev][1])
