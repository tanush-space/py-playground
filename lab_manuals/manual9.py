'''9.	  Write a program to implement
●	Break Statement
●	Continue Statement
●	Pass Statement
'''

for i in range(1,6):
    if i==3:
        break
    print("Break Example:",i)

for i in range(1,6):
    if i==3:
        continue
    print("Continue Example:",i)

for i in range(1,6):
    if i==3:
        pass
    print("Pass Example:",i)
