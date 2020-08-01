#!/usr/bin/env python3
# Program convert different units according to user input
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/timer.py
# IDE PyCharm
# Python 3.8 compatible

import time
import os
import sys
from playsound import playsound

# User enter time for timer and is separated into hours, minutes and seconds and Error Handling
try:
    user_time = str(input("Please enter Timer you want in HOURS:MINUTES:SECONDS format "))
    hrs, minutes, sec = [int(s) for s in user_time.split(":") if s.isdigit()]
    seconds = (hrs * 60 * 60) + (minutes * 60) + sec
    current_time = time.time()
    add_time = current_time + seconds
    start_timer = time.gmtime(add_time - current_time)
except ValueError as e:
    print("Please enter correct value in right format")
    sys.exit(0)


# Check for time and print if second is reduced by comparing with current time better then time.sleep() function
while True:
    try:
        timer = time.gmtime(add_time - time.time())
        if timer < start_timer:
            os.system("cls||clear")
            time_str = time.strftime("%H hour, %M minutes, %S seconds ", timer)
            print(time_str)
            start_timer = timer
        elif time.time() > add_time:
            os.system("cls||clear")
            print("Times up")
            playsound("https://onlineclock.net/audio/options/default.mp3")
            break
    except KeyboardInterrupt:
        sys.exit(0)
