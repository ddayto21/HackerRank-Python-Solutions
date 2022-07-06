# GOAL: LEARN HOW TO MANIPULATE ELEMENTS IN A DICTIONARY
from collections import Counter

# GOAL: CREATE A DICTIONARY USING THE 'COLLECTIONS' MODULE  
input_arr = [3,3,2,1,3]
arr_count = Counter(input_arr)

input_str = "skeuwacekkkww"
str_count = Counter(input_str)
# print(str_count)

# GOAL: PRINT A LIST OF TUPLIES (KEY, VALUE)
for item in str_count.items():
    print(f"item: {item}")

# GOAL: UNPACK KEYS IN DICTIONARY USING THE *(ASTERISK) 
# print(*str_count)

# GOAL: FIND KEY WITH THE MAXIMUM VALUE IN THE DICTIONARY
max_key = max(str_count, key=str_count.get)
print("Key with maximum value in the dictionary: ", max_key)

# GOAL: find THE MAXIMUM VALUE IN THE DICTIONARY
max_value = max(str_count.values())
print("The maximum value in the dictionary is ", max_value)

