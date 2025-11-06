'''Write a program to implement tuple inbuilt functions.'''
t=tuple(map(int,input("Enter numbers separated by space: ").split()))
print("Tuple:",t)
print("Length:",len(t))
print("Max value:",max(t))
print("Min value:",min(t))
print("Sum:",sum(t))
print("Count of 1:",t.count(1))
print("Index of first element:",t.index(t[0]))
