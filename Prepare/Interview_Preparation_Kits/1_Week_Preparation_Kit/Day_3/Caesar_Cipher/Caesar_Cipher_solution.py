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
    for i in range(len(r_list)):
        curr_ord = ord(r_list[i])
        k = k % 26
        if (curr_ord >= 65) & (curr_ord <= 90):
            new_ord = curr_ord + k
            if (new_ord > 90):
                new_ord = new_ord - 26
                
            r_list[i] = chr(new_ord) 
        elif(curr_ord >= 97) & (curr_ord <= 122):
            new_ord = curr_ord + k
            if (new_ord > 122):
                new_ord = new_ord - 26
                
            r_list[i] = chr(new_ord) 
        else:
            r_list[i] = chr(curr_ord) 

    return ''.join(r_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
