#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    sumDR = 0
    sumDL = 0
    for i in range(0, len(arr)):
        sumDR += arr[i][i]
        sumDL += arr[i][len(arr) -i -1]

    if (sumDR > sumDL):
        return sumDR - sumDL
    elif (sumDR < sumDL):
        return sumDL - sumDR
    
    return 0
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
