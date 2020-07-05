#!/usr/bin/env python3
# Find Fibonacci Sequence till Nth Digit
# Program generate Fibonacci Sequence till user want
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/fibonacci_sequence.py
# IDE: PyCharm
# Version: Python 3.5 compatible


# Function to calculate fibonacci value
def compute_fibo(n):
    n1, n2 = 0, 1
    count = 0
    while count < n:
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1


# Ask for user input and handle Value Error
while True:
    try:
        value = input("Please enter number up to fibonacci_sequence calculate ")
        n = int(value)
        compute_fibo(n)
        break
    except ValueError:
        respond = input("Invalid Input. Press 'y' to Try Again or 'x' to Exit ")
        if respond == 'y' or respond == 'Y':
            continue
        else:
            break
