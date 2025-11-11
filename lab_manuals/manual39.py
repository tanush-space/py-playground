'''Write a program to create class student ,implement methods and access through its object .'''

class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.roll)
        print("Marks:",self.marks)

n=input("Enter name: ")
r=int(input("Enter roll no: "))
m=float(input("Enter marks: "))
s1=Student(n,r,m)
s1.display()
