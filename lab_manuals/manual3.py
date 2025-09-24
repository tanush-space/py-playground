'''3. Write a program to input the marks of 5 subjects and then calculate ● Total Marks Obtained ● Percentage of Marks ● Display grade'''

m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))
m4=int(input("Enter marks of subject 4: "))
m5=int(input("Enter marks of subject 5: "))
total=m1+m2+m3+m4+m5
per=total/5
print("Total Marks:",total)
print("Percentage:",per)
if per>=90:
    print("Grade: A")
elif per>=75:
    print("Grade: B")
elif per>=50:
    print("Grade: C")
else:
    print("Grade: F")
