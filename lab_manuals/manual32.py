# Write a program to Iterate through a dictionary using a for loop.
n=int(input("Enter number of items: "))
d={}
for i in range(n):
    k=input("Enter key: ")
    v=input("Enter value: ")
    d[k]=v
print("Dictionary items:")
for key in d:
    print(key,":",d[key])
