# Write a program to remove items from the set using
# •	Discard()
# •	Remove()
# •	Pop()

s=set(input("Enter elements separated by space: ").split())
x=input("Enter element to discard: ")
s.discard(x)
print("After discard:",s)
y=input("Enter element to remove: ")
s.remove(y)
print("After remove:",s)
print("Popped element:",s.pop())
print("After pop:",s)
