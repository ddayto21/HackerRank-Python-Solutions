# GOAL: ROTATE AN ARRAY 
arr = [1, 2,  3,  4,   5,   6] # Length = 6
# idx:  0  1   2   3    4   5 
# idx: -6  -5  -4  -3  -2  -1

# rot_arr = [6,1,2,3,4,5]
# TASK: RETURN THE LAST ELEMENT OF THE ARRAY
print(f"Last element of the array: {arr[-1]}")

# ROTATION: MOVE ALL ELEMENTS IN ARRAY TO THE RIGHT
def shift_right(arr):
    rot_arr = [arr[-1]]
    for i in range(0, len(arr)-1):
        rot_arr.append(arr[i])
    return rot_arr
rot_arr = shift_right(arr)
# print("Rotated Array: ", rot_arr)

# ROTATION: MOVE ELEMENTS IN THE ARRAY TO THE LEFT
# EXAMPLE:
    # arr = [1,2,3] --> [2,3,1]  --> [3,1,2]
        # rot[0] = arr[1]
        # rot[1] = arr[2]
        # rot[2] = arr[]        
input_arr = [1,3,4,2]
def shift_left(arr):
    rot_arr = []
    for i in range(len(arr)-1):
        rot_arr.append(arr[i+1])
        # print("rot_arr: ", rot_arr)
    rot_arr.append(arr[0])
    return rot_arr

for i in range(3):
    input_arr = shift_left(input_arr)
    print(f"Rotation {i}: {input_arr}")


    
    
