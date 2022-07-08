#!/bin/python3

import math
import os
import random
import re
import sys

# PROBLEM: Given an array of integers and a positive integer , determine the number of pairs where and + is divisible by . 
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

# GOAL: Return the number of pairs(i,j) that meet the following criteria:
        # Criteria (1): i < j 
        # Criteria (2): The sum of the pairs is divisible by k 
            # --> (ar[i] + ar[j]) % k  == 0
    
# =====  EXAMPLE PROBLEM (1)  ===== #
    # ==== INPUTS === #
        # n = 6
        # k = 3
        # ar = [1, 3, 2, 6, 1, 2]
    # === OUTPUT === #
        # result = 3 -->  Three pairs meet the criteria: [1,4], [2,3], [4,6]

# === SOLUTION === #
# STEP 1: Use a 'count' variable to keep track of valid pairs
# STEP 2: Use a nested for-loop to generate every possible combination of pairs in the array
# STEP 3: For each pair, check if they meet the following criteria:
    # (1): i < j 
    # (2): The sum of the pairs is divisible by k 
    # --> (ar[i] + ar[j]) % k  == 0

# STEP 3: If a pair meets both conditions, increment the count by 1


def divisibleSumPairs(k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            pair = ar[i:j+1]
            p_sum = sum(pair)
            if (pair[0] < pair[1]) and (p_sum % k == 0):
                count += 1                
    return count                

if __name__ == '__main__':
    input_arr = [1, 3, 2, 6, 1, 2]
    k = 5 # Divide (ar[i] + ar[j) by 'k' value 
    result = divisibleSumPairs(k, input_arr)
    
