#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'divisibleSumPairs' function below.        
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER n -> Length of ar    
    #  2. INTEGER k -> Number     
    #  3. INTEGER_ARRAY -> 
    
    # GOAL: Return the number of pairs (i, j) that meet the following criteria:
        # (1) i < j 
        # (2) The sum of the pairs is divisible by k 
            # --> ar[i] + ar[j]) % k  == 0
    # EXAMPLE 1: 
    # ==== INPUTS ===== #
        # n = 6
        # k = 3
        # ar = [1, 3, 2, 6, 1, 2]
    # APPROACH
        # (*) Sort array in ascending order 
        # (*) Use a nested for-loop to generate every possible combination of pairs in the array
        # for i in range(0, len(ar)-1):
            # for j in range(i+1, len(ar)):
            #  if (i < j) and (sum(i,j) % k) == 0
            

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            pair = ar[i:j+1]
            print("Pair:")
            p_sum = sum(pair)
            if (pair[0] < pair[1]) and (p_sum % k == 0):
                count += 1
                
    return count
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
