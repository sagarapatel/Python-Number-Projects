#!/usr/bin/env python3
# Program convert different units according to user input
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/calculator.py
# IDE PyCharm
# Python 3.8 compatible

# Dict[int, Dict[int, Tuple[str, str]]]
unit = {
    1: {
        12: ("(x * 9/5) + 32", "Celsius"),
        21: ("(x-32) * 5/9", "Ferenheit")
    },
    2: {
        12: ("x * 1000", "Kilogram")
    }
}


def selection(num_one, num_two):
    merge_sel = int(str(num_one) + str(num_two))
    reverse_sel = int(str(merge_sel)[::-1])
    return merge_sel, reverse_sel


print("Welcome to unit conversion ")
print("Please select one of the Conversions")
d_one = int(input("1 for Temperature \n2 for Mass\n"))
if d_one == 1:
    print("\nSelect temperature unit you would like to convert FROM")
    sel_one = int(input("1 for {}\n2 for {}\n".format(unit[d_one][12][1], unit[d_one][21][1])))
    print("\nSelect temperature unit you would like to convert TO")
    sel_two = int(input("1 for Celsius\n2 for Fahrenheit\n"))
    d_two, d_two_re = selection(sel_one, sel_two)
elif d_one == 2:
    print("\nSelect Mass unit you would like to convert FROM")
    sel_one = int(input("1 for Kilogram\n2 for Gram\n3 for Milligram\n"))
    print("\nSelect Mass unit you would like to convert TO")
    sel_two = int(input("1 for Kilogram\n2 for Gram\n3 for Milligram\n"))
    d_two, d_two_re = selection(sel_one, sel_two)

x = int(input("\nPlease Enter value to convert "))
formula = unit[d_one][d_two][0]
print(str(x) + " " + unit[d_one][d_two][1] + " = " + str(eval(formula)) + " " + unit[d_one][d_two_re][1])
