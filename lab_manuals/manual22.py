'''Write a program to enter the values of a tuple at run time.'''

num_elements = int(input("Enter the number of elements in the tuple: "))
print("Enter the elements:")
tuple_elements = []
for _ in range(num_elements):
    element = input("> ")
    tuple_elements.append(element)
user_tuple = tuple(tuple_elements)
print("The created tuple is:", user_tuple)
