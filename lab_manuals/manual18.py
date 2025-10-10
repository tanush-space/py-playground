'''18	Write a program of list to implement using inbuilt functions
•	Find the length of a list using len ().
•	Check if an element exists in a list using in keyword.
•	Sort a list using sort () or sorted ().
•	Reverse a list using reverse ().
•	Copy a list using slicing or copy ().
'''
lst=list(map(int,input("Enter numbers separated by space: ").split()))
print("List:",lst)
print("Length of list:",len(lst))
x=int(input("Enter number to check: "))
print("Exists in list:",x in lst)
lst.sort()
print("Sorted list:",lst)
lst.reverse()
print("Reversed list:",lst)
copy1=lst[:]
copy2=lst.copy()
print("Copy using slicing:",copy1)
print("Copy using copy():",copy2)
