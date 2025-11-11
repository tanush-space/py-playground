'''Write a program to implement multiple classes.'''

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def show(self):
        print("Name:",self.name)
        print("Roll No:",self.roll)

class Marks:
    def __init__(self,subject,score):
        self.subject=subject
        self.score=score

    def show(self):
        print("Subject:",self.subject)
        print("Score:",self.score)

s=Student(input("Enter name: "),int(input("Enter roll no: ")))
m=Marks(input("Enter subject: "),float(input("Enter score: ")))

s.show()
m.show()
