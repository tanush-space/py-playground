'''Write a program to generate fibonacii series using recursion.'''

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

num=int(input("Enter number of terms: "))
for i in range(num):
    print(fib(i))
