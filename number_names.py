#!/usr/bin/env python3
# Program shows how to spell the numbers in english up to one million
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/number_names.py
# IDE PyCharm
# Python 3.8 compatible

# Dictionary specify names to numbers
ones = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}
tens = {
    1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen"
}
count = {
    3: "hundred", 4: "thousand", 6: "hundred"
}

# User input integer number
x = int(input("Please enter positive number to convert into words "))
length = len(str(x))
skip = 0
# Iterate through the numbers
for n in str(x):
    digit = int(n)
    # IF block for ones digit
    if digit in ones and length in (1, 3, 4, 6) and digit != 0 and skip == 0:
        print(ones[digit], end=" ")
    # IF block for words between numbers
    if (length in count and length in (3, 4, 5, 6) and digit != 0) or (length == 4 and digit == 0):
        print(count[length], end=" ")
        skip = 0
    # IF block for numbers in tens
    if length in (2, 5) and digit != 0:
        if digit == 1 and length == 2:
            digit = abs(x) % 100
            skip = 1
        elif digit == 1 and length == 5:
            digit = str(x)[-5:-3]
            skip = 1
        print(tens[int(digit)], end=" ")
    # IF block for number zero
    if length == 1 and x == 0:
        print("Zero")
    length -= 1
