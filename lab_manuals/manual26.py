'''26 Write a program to add items in the set using • Add method • Using Update method'''

s=set(input("Enter elements separated by space: ").split())
x=input("Enter element to add: ")
s.add(x)
print("After add:",s)
new=set(input("Enter elements to update separated by space: ").split())
s.update(new)
print("After update:",s)
