'''Write a program to create a dictionary and access values using keys.'''
n=int(input("Enter number of items: "))
d={}
for i in range(n):
    k=input("Enter key: ")
    v=input("Enter value: ")
    d[k]=v
print("Dictionary:",d)
key=input("Enter key to access value: ")
print("Value:",d[key])
