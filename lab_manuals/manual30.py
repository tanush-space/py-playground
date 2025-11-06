'''Write a program to delete keys value from a dictionary.'''

n=int(input("Enter number of items: "))
d={}
for i in range(n):
    k=input("Enter key: ")
    v=input("Enter value: ")
    d[k]=v
print("Original dictionary:",d)
key=input("Enter key to delete: ")
if key in d:
    del d[key]
    print("After deletion:",d)
else:
    print("Key not found")
