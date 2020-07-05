#!/usr/bin/env python3
# Find prime numbers until user ask
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/prime_number.py
# IDE PyCharm
# Python 3.5 compatible


def prime_number():
    for i in range(2, 100):
        n = input("Enter 'y' for next prime number or Any other key to Exit ")
        if n == 'y' or n == 'Y':
            for num in range(2, i):
                if (i % num) == 0:
                    break
            else:
                print(str(i) + " is a prime number")
        else:
            print("Thank you")
            break


prime_number()
