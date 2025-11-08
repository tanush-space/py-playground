'''Write a program to implement Inbuilt
•	Math functions
•	String functions
'''
import math

print("Math Functions:")
x=float(input("Enter a number: "))
print("Square root:",math.sqrt(x))
print("Power (x^2):",math.pow(x,2))
print("Ceil:",math.ceil(x))
print("Floor:",math.floor(x))

print("\nString Functions:")
s=input("Enter a string: ")
print("Uppercase:",s.upper())
print("Lowercase:",s.lower())
print("Title:",s.title())
print("Length:",len(s))
print("Replaced string:",s.replace('a','@'))
