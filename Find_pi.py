
# Find PI to the Nth Digit
# Program generate PI with decimal places up to value of n
# Limit upto 400 decimal places.
# Ref: https://www.math.hmc.edu/funfacts/ffiles/20010.5.shtml
# Github: https://github.com/sagarapatel/Python-Number-Projects/blob/master/Find_pi.py

from __future__ import division
import math
import decimal
from decimal import Decimal
from decimal import getcontext


def compute_pi(n):
    maximum = 10000
    decimal.getcontext().prec = n + 1
    pi = Decimal(0)

    for k in range(maximum):
        pi += Decimal(math.pow(16, -k)) * (Decimal(4 / (8 * k + 1)) - Decimal(2 / (8 * k + 4)) -
                                           Decimal(1 / (8 * k + 5)) - Decimal(1 / (8 * k + 6)))
    return pi


n = 100
print(compute_pi(n))
