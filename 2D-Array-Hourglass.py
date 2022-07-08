#!/bin/python3

import math
import os
import random
import re
import sys

# PROBLEM: Given a 2D Array (6x6), return the max hourglass sum 

# ==== EXAMPLE PROBLEM ======:
# INPUT: 
    # arr = [
          # [1, 1, 1, 0, 0, 0],
          # [0, 1, 0, 0, 0, 0],
          # [1, 1, 1, 0, 0, 0], 
          # [0, 0, 2, 4, 4, 0],
          # [0, 0, 0, 2, 0, 0],
          # [0, 0, 1, 2, 4, 0]
          #                    ]

#  ---- GRAPHICAL REPRESENTATION ---- #                    
                    # ==== COLUMNS ==== #
#                       0 1 2 3 4 5

        #   ROW 0   |   1 1 1 0 0 0
        #   ROW 1   |   0 1 0 0 0 0
        #   ROW 2   |   1 1 1 0 0 0
        #   ROW 3   |   0 0 2 4 4 0
        #   ROW 4   |   0 0 0 2 0 0
        #   ROW 5   |   0 0 1 2 4 0

# APPROACH:
# (1) SUBSET THE MATRIX TO GET HOURGLASS CELLS (7)
# --- HOURGLASS PATTERN --- #
    #   a b c
    #     d
    #   e f g 

    # === HOURGLASS #1 === #
        # 1 1 1
        #   1
        # 1 1 1
                # a -> arr[0][1] = 1
                # b -> arr[0][2] = 1
                # c -> arr[0][3] = 1
                # d -> arr[1][2] = 1
                # e -> arr[2][1] = 1
                # f -> arr[2][2] = 1
                # g -> arr[2][3] = 1

        # --- HOURGLASS #1 SUM --- #
        # -> sum(hourglass) = 7

    # === HOURGLASS #2 === #
        # 1 1 0
        #   0
        # 1 1 0
                # a -> arr[0][0] = 1  ** i=0, j=0 **
                # b -> arr[0][1] = 1  ** i=0, j=1**
                # c -> arr[0][2] = 0
                # d -> arr[1][1] = 0
                # e -> arr[2][0] = 1
                # f -> arr[2][1] = 1
                # g -> arr[2][2] = 0
        
    # --- HOURGLASS #2 SUM --- #
        # -> sum(hourglass) = 4
    
# APPROACH:
    # == VARIABLES == #
    # max_sum = 0

    # STEP 1: Subset array to get hourglass pattern (x16)    
    # STEP 2: Calculate sum of each hourglass [curr_sum]
    # STEP 3: Compare the max_sum to the curr_sum



def hourglassSum(arr):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()