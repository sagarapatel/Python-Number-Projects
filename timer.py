#!/usr/bin/env python3
# Program convert different units according to user input
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/timer.py
# IDE PyCharm
# Python 3.8 compatible

import time
import os
import sys

hours = 0
minutes = 1
seconds = minutes * 60
current_time = time.time()
add_time = current_time + seconds
start_timer = time.gmtime(add_time - time.time())


while True:
    try:
        timer = time.gmtime(add_time - time.time())
        if timer < start_timer:
            os.system("cls")
            time_str = time.strftime("%H hour, %M minutes, %S seconds ", timer)
            print(time_str)
            start_timer = timer
        elif time.time() > add_time:
            os.system("cls")
            print("Time up")
            break
    except KeyboardInterrupt:
        sys.exit(0)
