#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    #count the frequency of each element on the array
    count_arr = Counter(arr)
    count_brr = Counter(brr)
    
    #Find the missing number 
    missing = []
    for num in count_brr:
        if count_brr[num] > count_arr.get(num,0):
            missing.append(num)
            
    return sorted(missing)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
