# URL: https://programs.programmingoneonone.com/2021/01/hackerrank-day-12-inheritance-solution.html

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = map(int, scores)

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg <= 100 and avg >= 90:
            return 'O'
        if avg <= 90 and avg >= 80:
            return 'E'
        if avg <= 80 and avg >= 70:
            return 'A'
        if avg <= 70 and avg >= 55:
            return 'P'
        if avg <= 55 and avg >= 40:
            return 'D'
        else:
            return 'T'