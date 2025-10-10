''''Write a program to implement list methods
•	Use count () to count occurrences of an element.
•	Use index () to find the index of an element.
•	Use extend () to add elements from another list.
•	Use pop () to remove and return an element.
•	Use clear () to remove all elements from a list.
'''
lst=list(map(int,input("Enter numbers separated by space: ").split()))
print("List:",lst)
x=int(input("Enter number to count: "))
print("Count of",x,":",lst.count(x))
y=int(input("Enter number to find index: "))
print("Index of",y,":",lst.index(y))
new=list(map(int,input("Enter another list to extend: ").split()))
lst.extend(new)
print("After extend:",lst)
print("Popped element:",lst.pop())
print("After pop:",lst)
lst.clear()
print("After clear:",lst)
