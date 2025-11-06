'''Write a program to create a student class and instantiate objects'''

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

n=input("Enter student name: ")
a=int(input("Enter student age: "))
s1=Student(n,a)
s1.show()
