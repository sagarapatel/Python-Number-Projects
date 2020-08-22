#!/usr/bin/env python3
# Program shows how to spell the numbers in english up to one million
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/number_names.py
# IDE PyCharm
# Python 3.8 compatible

ones = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}
tens = {
    1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
}
count = {
    3: "hundred", 4: "thousand"
}

x = 3143
length = len(str(x))
for n in str(x):
    digit = int(n)
    if digit in ones and length > 2 and digit != 0:
        print(ones[digit])
    if length in count and digit in ones and length > 2 and digit != 0:
        print(count[length])
    if length == 2 and digit != 0:
        print(tens[digit])
    if length < 2 and digit != 0:
        print(ones[digit])
    length -= 1
print(x)
