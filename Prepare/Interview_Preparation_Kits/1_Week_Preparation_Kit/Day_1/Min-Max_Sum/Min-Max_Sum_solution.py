#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sumE0 = 0
    sumE1 = 0
    sumE2 = 0
    sumE3 = 0
    sumE4 = 0
    
    parr = [0]*5
    parr[0] = arr[1] + arr[2] + arr[3] + arr[4] 
    parr[1] = arr[0] + arr[2] + arr[3] + arr[4] 
    parr[2] = arr[0] + arr[1] + arr[3] + arr[4] 
    parr[3] = arr[0] + arr[1] + arr[2] + arr[4] 
    parr[4] = arr[0] + arr[1] + arr[2] + arr[3] 
    
    print(str(min(parr)) + " " + str(max(parr)))

    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

