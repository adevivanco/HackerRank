#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    r_list = list(s)
    for i in range(len(s)):
        curr_ord = ord(s[i])
        if (curr_ord >= 65) & (curr_ord <= 90):
            new_ord = curr_ord + k
            if (new_ord > 90):
                new_ord = 65 + (new_ord % 90 -1)
            r_list[i] = chr(new_ord) 
        elif(curr_ord >= 97) & (curr_ord <= 122):
            new_ord = curr_ord + k
            if (new_ord > 122):
                new_ord = 97 + (new_ord %122 -1)
            r_list[i] = chr(new_ord) 

    return  ''.join(r_list)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

