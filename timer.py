#!/usr/bin/env python3
# Program convert different units according to user input
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/timer.py
# IDE PyCharm
# Python 3.8 compatible

import time
import sys
import os

hours = 0
minutes = 10
seconds = minutes * 60
start_time = time.time()
y = current_time = time.gmtime((start_time + seconds) - time.time())


while True:
    try:
        current_time = time.gmtime((start_time + seconds) - time.time())
        time_str = time.strftime("%M minutes, %S seconds ", current_time)
        x = current_time
        if x < y:
            os.system("cls")
            print(time_str)
            y = x
        sys.stdout.flush()
    except KeyboardInterrupt:
        break
