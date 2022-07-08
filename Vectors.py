import numpy as np
x = [1, -1, 1]
y = [4, 2, 3]
print("Vector X: ", x)
print("Vector Y: ", y)
# z = np.cross(x,y)
# print("Cross Product: ", z) # [-5  1  6]

def cross_product(x,y):
    return np.cross(x,y)

def dot_product(x,y):
    return np.dot(x,y)


