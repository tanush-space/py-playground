'''29	Write a program to update existing keys value in a dictionary.'''
n=int(input("Enter number of items: "))
d={}
for i in range(n):
    k=input("Enter key: ")
    v=input("Enter value: ")
    d[k]=v
print("Original dictionary:",d)
key=input("Enter key to update: ")
if key in d:
    val=input("Enter new value: ")
    d[key]=val
    print("Updated dictionary:",d)
else:
    print("Key not found")
