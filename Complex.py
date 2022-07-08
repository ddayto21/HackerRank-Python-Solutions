# === COMPLEX NUMBERS ==== #
# Complex Numbers have 2 Parts: (Real, Imaginary) 
# EXAMPLE:
    #  2+5j 
        # 2 -> Real Number (number without 'j' attached)
        # 5 -> Imaginary Number (number with 'j' attached)

class Complex ():
    def initComplex(self):
        self.realPart = int(input("Enter the Real Part: "))
        self.imgPart = int(input("Enter the Imaginary Part: "))            
    def display(self):
        print(self.realPart,"+",self.imgPart,"i", sep="")
    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart

c1 = Complex()
c2 = Complex()
c3 = Complex()

print("Enter first complex number")
c1.initComplex()
print("First Complex Number: ", end="")
c1.display()
print("Enter second complex number")
c2.initComplex()
print("Second Complex Number: ", end="")
c2.display()
print("Sum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()


# import math, cmath, numpy

# # COMPLEX OPERATIONS:
# # --- ADDITION --- #
# # APPROACH:  (a + bi)+ (c + di) = (a + c) + (b + d)i 

# # COMPLEX NUMBER REQUIREMENTS:
#     # (1) Use integers, not float values
#     # (2) Use the variable 'j'

# # === EXAMPLE === #
# complex_one = 2 + 1j
# complex_two = 5 + 6j

#  = cmath.phase(C)
# print(phase)


# # STEP (1): Parse the elements of the expression
# # STEP (2): Get the real numbers from the expression
# # STEP (3): Get the imaginary numbers from the expression

# # VARIABLES
#     # a = 2.0
#     # b = 1.0
#     # c = 5.0
#     # d = 6.0

# # OPERATIONS:
# # --> (2.0 + 6.0) + (1.0 + 6.0)i
# # RESULT = 8.0 + 7.0i

# # PROBLEM: Given two complex numbers, print the result of the following operations:
#     # Addition
#     # Subtraction 
#     # Multiplication
#     # Division
#     # Modulus 

# # OPERATIONS [COMPLEX NUMBERS]
#     # FORMULA:  (a + bi)+ (c + di) = (a + c) + (b + d)i
#         # EXAMPLE 1: (2 + 7i) + (3 - 4i) 
# #             # --> (2 + 3) + (7 - 4)i = 5 + 3i

# # class Complex(object):
# #     def __init__(self, real, imaginary):
# #         pass
        
# #     def __add__(self, no):
# #         pass
        
# #     def __sub__(self, no):
# #         pass
        
# #     def __mul__(self, no):
# #         pass

# #     def __truediv__(self, no):
# #         pass

# #     def mod(self):
# #         pass

# #     def __str__(self):
# #         if self.imaginary == 0:
# #             result = "%.2f+0.00i" % (self.real)
# #         elif self.real == 0:
# #             if self.imaginary >= 0:
# #                 result = "0.00+%.2fi" % (self.imaginary)
# #             else:
# #                 result = "0.00-%.2fi" % (abs(self.imaginary))
# #         elif self.imaginary > 0:
# #             result = "%.2f+%.2fi" % (self.real, self.imaginary)
# #         else:
# #             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
# #         return result

# # if __name__ == '__main__':
# #     c = map(float, input().split())
# #     d = map(float, input().split())
# #     x = Complex(*c)
# #     y = Complex(*d)
# #     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')