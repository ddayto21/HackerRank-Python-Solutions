import math

# PROBLEM: Given two complex numbers, print the result of the following operations:
    # Addition
    # Subtraction 
    # Multiplication
    # Division
    # Modulus 

# === PREREQUISITES ===== @
# PREREQUISITE(1): COMPLEX NUMBERS 
    # DESCRIPTION: Complex Numbers have 2 Parts: (Real, Imaginary) 
    # USE CASES: 
        # (1)
    # EXAMPLES: 
        #  2+5j 
            # 2 -> Real Number (number without 'j' attached)
         # 5 -> Imaginary Number (number with 'j' attached)
    
# PREREQUISITE(2): BUILT-IN METHODS (DUNDER METHODS)
    # DESCRIPTION: Methods that have double underscores on both sides of the method name (__add__)
        # https://python-course.eu/oop/magic-methods.php
    # USE CASES: 
        # (1) Implement overloaded operators 
        # (2) Implement additional built-in functionality
    # EXAMPLES: 
        # __init__
        # __str__ --> Customize the string representation of an instance of a class.
        # __add__ 
        # __sub__
        # __mul__
        # __truediv__
    # FUNCTIONS: 
        # dir() --> Return an array of dunder methods inherited by a class
        
# PREREQUISITE(3): FORMAT SPECIFIERS 
    # USE CASES:
        # (1) Format a 'float' variable 
        # (2) Round a 'float' variable and display as a string

    # IMPLEMENTATION: 
        # (1) Add '%.' to string:
            # >>> "%."
        # (2) Define the number of decimal points:
            # >>> "%.3"
        # (3) Specify data type:
            # >>> "%.3f" ---> f(float)            
        # (4) Add '% (variable_name)' to the string
                # =====  EXAMPLE === #
                    #  input_float = 39.545917324
                        # >>> print("%.2f" % input_float) --> 39.54
                        # >>> print("%.3f" % input_float) --> 39.545
    # USE CASES:
        # (1) Round value to product a string to display to user
            # >>> print(%.2f) % (39.5448298234)
                # >>> 39.54

#  input_float = 39.5442984722354987

print("%.3f" % input_float)

# OPERATIONS [COMPLEX NUMBERS]
    # FORMULA:  (a + bi)+ (c + di) = (a + c) + (b + d)i
        # EXAMPLE 1: (2 + 7i) + (3 - 4i) 
            # --> (2 + 3) + (7 - 4)i = 5 + 3i

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        pass
        
    def __sub__(self, no):
        pass
        
    def __mul__(self, no):
        pass

    def __truediv__(self, no):
        pass

    def mod(self):
        pass

    def __str__(self):
        print("__str__ method: \n")
        print(self.__dict__) # {'real': 5.0, 'imaginary': 6.0}
        print("-------------------")
        if self.imaginary == 0:
            print("imaginary number is 0")
            result = "%.2f+0.00i" % (self.real)
            print("result: ", result)
        elif self.real == 0:
            if self.imaginary >= 0:
                print("imaginary number is greater than or equal to 0")
                result = "0.00+%.2fi" % (self.imaginary)
                print("result: ", result)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
                print()
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')