import numpy

# PROBLEM: Print a reversed NumPy array with the element type float
# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true

# APPROACH:
    # (1) Convert original array to a NumPy array
    # (2) Use list comprehension to create a reversed NumPy array
    # (3) Use the .round() method to set the number of decimals to 0

def arrays(arr):
    np_arr = numpy.array(arr, float)
    # print(np_arr)
    # Set number of decimal points to 0
    rev_arr = numpy.array([x for x in reversed(np_arr)])
    result = rev_arr.round(0)
    # print("result: ", result)
    return result
    
arr = input().strip().split(' ')
result = arrays(arr)
# print(result)