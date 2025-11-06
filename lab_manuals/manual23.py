# Write a program to implement basic tuple operations (+,*,in).

t1=tuple(input("Enter elements of first tuple separated by space: ").split())
t2=tuple(input("Enter elements of second tuple separated by space: ").split())
print("Concatenation:",t1+t2)
print("Repetition:",t1*2)
x=input("Enter element to check: ")
print("Exists in first tuple:",x in t1)
