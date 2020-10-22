# https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        scores_avg = sum(scores)/len(scores)

        if scores_avg >= 90:
            letter = 'O'
        elif scores_avg >= 80:
            letter = 'E' 
        elif scores_avg >= 70:
            letter = 'A' 
        elif scores_avg >= 55:
            letter = 'P' 
        elif scores_avg >= 40:
            letter = 'D' 
        elif scores_avg < 40:
            letter = 'T'
        
        return letter

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
