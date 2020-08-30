#!/usr/bin/env python3
# Program simulates coin flip and gives output of heads or tail
# Github: https://github.com/sagarapatel/Python-Number-Projects/blob/master/coin_flip.py
# IDE: PyCharm
# Version: Python 3.8 compatible

from numpy import random
h = 0
t = 0

while True:
    x = input("Would you like to flip coin 'y' for Yes and 'n' for No ")
    if x in ('y', 'Y', 'Yes', 'yes'):
        # Using binomial get either 0 or 1 as output with probability of 0.5 (equal)
        coin = random.binomial(1, 0.5)
        if coin == 0:
            print("Heads")
            h += 1
        else:
            print("Tails")
            t += 1
    else:
        break
    print("Heads = {}".format(h))
    print("Tails = {}".format(t))
