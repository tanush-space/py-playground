'''15	Write a program to create a list and access elements using indexing and slicing.'''
lst=list(map(int,input("Enter numbers separated by space: ").split()))
print("List:",lst)
print("First element:",lst[0])
print("Last element:",lst[-1])
print("First three elements:",lst[:3])
print("Middle elements:",lst[1:-1])
print("Reversed list:",lst[::-1])
