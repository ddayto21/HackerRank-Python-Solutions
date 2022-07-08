# GOAL: LEARN HOW TO USE THE MAP() FUNCTION

# -- PARAMETERS -- #
    # (1) function - a function that perform some action to each element of an iterable
    # (2) iterable - an iterable like sets, lists, tuples, etc
    
    # --> map(function, iterable)
numbers = [1,2,3,4,5]

def calculateSquare(n):
    return n * n
result = map(calculateSquare, numbers)

# --- UNPACK ITERABLE USING ASTERISK(*) -- #
print(*result) # --> 1 4 9 16 25 

    





