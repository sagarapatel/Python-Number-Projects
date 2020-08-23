#!/usr/bin/env python3
# Program shows how to spell the numbers in english up to one million
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/number_names.py
# IDE PyCharm
# Python 3.8 compatible

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

x = 17221
length = len(str(x))
for n in str(x):
    digit = int(n)
    if digit in ones and length in (3, 4, 6) and digit != 0:
        print(ones[digit])
    if (length in count and digit in ones and length in (3, 4, 5, 6) and digit != 0) or (length == 4 and digit == 0):
        print(count[length])
    if length in (2, 5) and digit != 0:
        if digit == 1 and length == 2:
            digit = abs(x) % 100
            length -= 2
        print(tens[digit])
    if length == 1 and digit != 0:
        print(ones[digit])
    length -= 1
print(x)
