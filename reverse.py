import numpy as np

arr = [1,2,3,4]

# METHOD 1: INDEXING 
res_arr = arr[::-1]
# print(f"Method 1: {res_arr}")

# METHOD 2: REVERSE() METHOD
copy = arr.copy()
copy.reverse()
# print(f"Method 2:  {copy}")

# METHOD 3: REVERSED() METHOD
rev = list(reversed(arr))
# print(f"Method 3: {rev}")

# METHOD 4: LIST COMPREHENSION
# print("Method 4: ", [x for x in reversed(arr)])

def reverse_array(arr):
    arr = np.array(arr)
    arr = arr.astype(float)
    rev_arr =  [x for x in reversed(arr)]
    return np.around(rev_arr)

rev_arr = reverse_array(arr)
print("Reversed Array: ", rev_arr)

