#!/usr/bin/env python3
# Convert Binary to Decimal and Back
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/binary_decimal.py
# IDE PyCharm
# Python 3.8 compatible


# Takes in Binary or Float number and convert it into vice versa.
while True:
    try:
        number = float(input("Please enter integer number to convert in decimal "))
        int_part, dec_part = str(number).split(".")
        # Converting string into integer and then into binary and then left strip 0b from value
        # Merging both binary values with decimal point
        print(bin(int(int_part)).lstrip("0b") + "." + bin(int(dec_part)).lstrip("0b"))
    except ValueError:
        print("Please enter correct integer number \n")
        continue
    try:
        binary = int(input("\nPlease enter binary value in 0 and 1 only "), 2)
        print(binary)
        break
    except ValueError:
        print("Please enter correct values in binary \n")
        continue
