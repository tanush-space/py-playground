'''10	Write a program to implement
•	Exception Handling
•	Else Statement
•	Custom exceptions
'''

class MyError(Exception):
    pass

try:
    n=int(input("Enter a number: "))
    if n<0:
        raise MyError("Negative number not allowed")
    print("Number is:",n)
except ValueError:
    print("Invalid input")
except MyError as e:
    print(e)
else:
    print("No exception occurred")

