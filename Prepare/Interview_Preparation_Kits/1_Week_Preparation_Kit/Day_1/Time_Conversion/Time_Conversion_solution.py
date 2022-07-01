#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[0:2])
    mins = int(s[3:5])
    sec = int(s[6:8])
    am_or_pm = s[8:10]
    
    if (am_or_pm == "PM"):
        if (hour != 12):
            hour = hour + 12
    else:
        if (hour == 12):
            hour = 0
            
    return str(hour).zfill(2) + ":" + str(mins).zfill(2) + ":" + str(sec).zfill(2)
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


