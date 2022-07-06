#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'birthday' function below.
    # The function is expected to return an INTEGER
    # The function accepts following parameters:
        #  1. INTEGER_ARRAY [s] -> Array of integers
        #  2. INTEGER [d] -> Birth Day
        #  3. INTEGER [m] -> Birth Month
            # m = size of the array (window)
        # SLIDING WINDOW APPROACH: 
            # (1) Use an array to keep track of valid combinations of chocolate
                # res_array = []
            # (2) Define a window of length m
                # window = [start:end]
                    # start = 0, end = m 
            # (3) Calculate the sum of the current window:
                # If the sum of the window equals the birth date, then append the window to the res_array:
                    # if sum(window) == d: res_array.append(window)
            
                    
    # GOAL: Return a set of arrays where the following criteria are met:
        # (1) len(arr) == m
        # (2) sum(arr) == d
        
def birthday(s, d, m):
    start, end = 0 , m
    res_array = []
    while end <= len(s):
        window = s[start:end]
        print("Window: ", window)
        if sum(window) == d:
            res_array.append(window)
        start += 1
        end += 1
    return len(res_array)               

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
