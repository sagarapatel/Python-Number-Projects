#!/usr/bin/env python3
# Generate prime numbers until user wants
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/prime_number.py
# IDE PyCharm
# Python 3.8 compatible

n = 'y'


# Function generate prime numbers individually until user wants
def prime_number(n):
    for i in range(2, 10000):
        if n == 'y' or n == 'Y':
            for num in range(2, i):
                if (i % num) == 0:
                    break
            else:
                print(str(i) + " is a prime number")
                n = input("Enter 'y' for next prime number or Any other key to Exit ")
        else:
            print("Thank you")
            break


prime_number(n)
