'''16	Write a program to modify list elements using assignment.'''
lst=list(map(int,input("Enter numbers separated by space: ").split()))
print("Original list:",lst)
i=int(input("Enter index to modify: "))
v=int(input("Enter new value: "))
lst[i]=v
print("Updated list:",lst)
