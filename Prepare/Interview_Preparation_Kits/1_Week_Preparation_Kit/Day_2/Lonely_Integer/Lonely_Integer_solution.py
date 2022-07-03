
# URL:  https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):

    # build dict
    dic = {}
    for n in a:
        if (n not in dic):
            dic[n] = 1
        else:
            dic[n] += 1
        
    # return the element that only has one occurence        
    for v in dic:
        if (dic[v] == 1):
            return v
            
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

