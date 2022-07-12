class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    def printname(self):
        print(f"My name is: {self.firstName} {self.lastName} ")

person = Person("Obi Wan", "Kenobi")
person.printname()