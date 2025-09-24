'''6. Write a program to calculate factorial of a no using while loop.'''
n=int(input("Enter a number: "))
f=1
i=1
while i<=n:
    f=f*i
    i+=1
print("Factorial:",f)
