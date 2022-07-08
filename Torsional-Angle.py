import math
import numpy as np
# PROBLEM: Given 4 Points (A,B,C,D) in a 3D Coordinate System

# ======== EXAMPLE CASE ========== #    
# == INPUTS == #
    # 0 4 5 -> A(0,4,5)
    # 1 7 6 -> B(1,7,6)
    # 0 5 9 -> C(0,5,9)
    # 1 7 2 -> D(1,7,2)

# PLANE 1 -> (A,B,C)
# PLANE 2 -> (B,C,D)

# === CALCULATIONS === #
    # Angle (PHI)
    # Cos(PHI) = (X.Y)/|X||Y|        
    # X = AB x BC  
        # AB x BC => Cross_Product(AB, BC)
            # AB = B - A
            # BC = C - B
    # Y = BC x CD 
        # BC x CD => Cross_Product(BC, CD)
            # BC = C - B
            # CD = D -C
    # X.Y -> Dot_Product(X,Y)
 
# === OUTPUT === # 
    # phi = angle[degrees])
        # Degrees displayed using up to two decimal places    

# ============= PREREQUISITES ========================== #
# --- PREREQUISITE (1): 3D CARTESIAN COORDINATES  ---
    # https://www.usna.edu/Users/oceano/raylee/SM223/Ch12_1_Stewart(2016).pdf

# --- PREREQUISITE (2): DOT PRODUCT ---
    # ---- USE CASES --- #
        # (1): Get the angle between two vectors
    #  --- CALCULATIONS -- #
        # ====== METHOD 1 ====== #
        # A.B = |A||B|cos(θ)
        # --- EXAMPLE INPUT --- #
            # A = [0,4,5]
            # B = [1,7,6]
                # MAGNITUDE CALCULATION 
                    # V = (x, y, z) is: |V| = √(x2 + y2 + z2)
                        # Step 1 - Find the sum of squares of each component
                        # Step 2 - Take the square root of the sum 
                        # --- EXAMPLE --- #
                        # ---- INPUT -- #
                            # V = (X,Y,Z)
                                # |V| = (x^2 + y^2 + z^2)^1/2
            # |B| = Magnitude(Vector B)
            # θ = Angle Between Vectors A and B
        # ====== METHOD 2 ====== #
        # A.B = A1*B1 + A2*B2 + A3*B3 ... 
            # A = [0,4,5]
            # B = [1,7,6]  
                # --- FUNCTION --- #
                    # DotProduct(A,B)
                        # (A[0]*B[0]) + (A[1]*B[1]) + (A[2]*B[2])        
                        # (0*1) + (4*7) + (5*6) -> 0 + 28 + 30 = 58
        # ===== METHOD 3 ===== #
            # A.B = numpy.dot(A,B)

                    
# --- PREREQUISITE (3): CROSS PRODUCT ---#
    # SOURCE: https://betterexplained.com/articles/cross-product/
    # ---- USE CASES ---- #
        # (1)  Calculate a vector that is perpendicular to two vectors
    # --- CALCULATION -- #
    #  METHOD 1: A x B = |A||B|sin(theta) 
            # |A| -> Magnitude (Vector A)
            # |B| -> Magnitude (Vector B)
            # theta(degrees) --> Angle Between Vectors A and B
    # METHOD 2: A x B = 
        # crossX = vector1.Y * vector2.Z - vector2.Y * vector1.Z
        # crossY = -(vector1.X * vector2.Z - vector2.X * vector1.Z)
        # crossZ = vector1.X * vector2.Y - vector2.X * vector1.Y
        # crossW = 0.0
        # --- EXAMPLE ---- # 
            #  u(1,2,3) x v(4,5,6) = ?
                #  ============ MATRIX DETERMINANT CALCULATION ============== #
                #                   |  i   j   k  |            |    i  j  k   |
                #    u x v    =>    |  u1  u2  u3 |      =>    |    1  2  3   |
                #                   |  v1  v2  v3 |            |    4  5  6   | 
    # METHOD 3: ----- NUMPY OPERATION ------
        # FUNCTION --> numpy.cross(a, b)
            # a: first vector
            # b: second vector
    # ==== APPROACH ==== #
    # STEP 1: CALCULATE X = (AB x BC)
        # (AB x BC) = (B-A) x (C-B)
    # ==== EXAMPLE INPUT ==== #    
        # 0 4 5 -> A(0,4,5)
        # 1 7 6 -> B(1,7,6)
        # 0 5 9 -> C(0,5,9)
        # 1 7 2 -> D(1,7,2)
            # (B-A) = (1-0, 7-4, 6-5) = (1,  3,  1)
            # (C-B) = (0-1, 5-7, 9-6) = (-1, -3, 3)
                # AB x BC = (1,3,1) x (-1,-3,3)
# STEP 2: CALCULATE Y
# STEP 3: CALCULATE 
             
class Points(object):
    def __init__(self, x, y, z):
        print("Initializing object... ")
        print("x: ", x)
        print("y: ", y)
        print("z: ", z)
        self.x = x
        self.y = y
        self.z = z
        print("self: ", self.__dict__)
        
    def __sub__(self, no):
        print("__sub__ method")
        print("self: ", self.__dict__) # self:  {'x': 1.0, 'y': 7.0, 'z': 6.0}
        print("no: ", no.__dict__) # no: {'x': 0.0, 'y': 4.0, 'z': 5.0}           

    def dot(self, no):
            u = [self.x, self.y, self.z]
            v = [no.x, no.y, no.z]
            print("Vector u: ", u)
            print("Vector v: ", v)
            dot_product = []
            for i in range(3):
                dot_product.append(u[i] * v[i])
            print("dot_product: ", dot_product)
            return dot_product    
    
    # Concept: Create a new vector [cross_x, cross_y, cross_z] 
    def cross(self, no):
        print("--- CROSS PRODUCT ---")
        print("self: ", self.__dict__)
        print("no: ", no)
        a = [self.x, self.y, self.z]
        b = [no['x'], no['y'], no['z']]
        print("Vector a: ", a)
        print("Vector b: ", b)
        cross_product = np.cross(a,b)
        return cross_product
                
            
    def absolute(self):
        print("--- MAGNITUDE ----")
        print("self: ", self.__dict__)
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        print(f" Enter 3D Coordinates for Point {i}:")
        a = list(map(float, input().split()))
        points.append(a)
    print(f"points: {points}") 
    # points: [[0.0, 4.0, 5.0], [1.0, 7.0, 6.0], [0.0, 5.0, 9.0], [1.0, 7.0, 2.0]]
    
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    print(f"a: {a.__dict__}") # a: {'x': 0.0, 'y': 4.0, 'z': 5.0}
    print(f"b: {b.__dict__}") # b: {'x': 1.0, 'y': 7.0, 'z': 6.0}
    print(f"c: {c.__dict__}") # c: {'x': 0.0, 'y': 5.0, 'z': 9.0}
    print(f"d: {d.__dict__}") # d: {'x': 1.0, 'y': 7.0, 'z': 2.0}
    # x = (b - a).cross(c - b)
    # x = (b-a).cross(c-b)
    x = (b - a).cross(c - b)
    print(x)
    # y = (c - b).cross(d - c)
    # angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    # print("%.2f" % math.degrees(angle))
