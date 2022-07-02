
# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    r = [0]*100
    
    for i in range(0, len(arr)):
        if (arr[i] < 100):    # this conidtion is necessary 
            r[arr[i]] += 1
        
    return r
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

