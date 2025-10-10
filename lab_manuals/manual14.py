'''14	Write a program to check whether the string is palindrome or not.'''
s=input("Enter a string: ")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
