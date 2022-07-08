class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self): # Methods that have double underscores (__method__) are invoked when an object is created using the class
        return f'Object: \n First Name: {self.first_name} Last Name: {self.last_name} Age: {self.age}'

Dan = Person('Dan', 'Bilzerian', 35)
# print("Dan: ", Dan) 

# TASK 1: DISPLAY THE STATE OF AN OBJECT 
    # IMPLEMENTATION:
        # (1) Add '.__dict__' after the name of the object
print(Dan.__dict__) # {'first_name': 'Dan', 'last_name': 'Bilzerian', 'age': 35}
