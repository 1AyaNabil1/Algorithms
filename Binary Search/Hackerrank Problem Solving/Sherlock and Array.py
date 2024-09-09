#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        # Right sum is total_sum minus the current element and left_sum
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return "YES"
        
        # Update left_sum for the next iteration
        left_sum += arr[i]
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
