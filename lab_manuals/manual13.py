'''Write a program count no of vowels, consonants, digits and length of the string.'''
s=input("Enter a string: ")
v=c=d=0
for i in s:
    if i.isdigit():
        d+=1
    elif i.lower() in 'aeiou':
        v+=1
    elif i.isalpha():
        c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("Length:",len(s))
