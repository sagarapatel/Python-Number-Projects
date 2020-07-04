#!/usr/bin/env python3

def compute_fibo(n):
    n1, n2 = 0, 1
    count = 0
    while count < n:
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1

value = input("Please enter number upto fibonacci_sequence ")
while True:
    try:
        n = int(value)
        compute_fibo(n)
        break
    except ValueError:
        break