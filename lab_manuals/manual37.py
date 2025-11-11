'''Write a program to calculate base to power of no using recursion.'''

def power(b,p):
    if p==0:
        return 1
    else:
        return b*power(b,p-1)

b=int(input("Enter base: "))
p=int(input("Enter power: "))
print("Result:",power(b,p))
