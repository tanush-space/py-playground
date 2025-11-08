'''Write a program to check whether the no is Armstrong or not using functions.'''
def is_armstrong(n):
    s=0
    t=n
    while t>0:
        d=t%10
        s+=d**3
        t//=10
    return s==n

n=int(input("Enter a number: "))
if is_armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")
