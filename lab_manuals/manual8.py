'''8. Write a program to calculate base to power of a no using while loop.'''
b=int(input("Enter base: "))
p=int(input("Enter power: "))
r=1
i=1
while i<=p:
    r=r*b
    i+=1
print("Result:",r)
