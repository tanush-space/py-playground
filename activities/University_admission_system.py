'''University Admission System
Write a program that takes marks in Physics, Chemistry, and Math.
•	Calculate total and average.
Admission Criteria:
•	Average ≥ 70 and each subject ≥ 60 → "Eligible for Admission"
•	Else if Math ≥ 90 → "Eligible under Math Special Quota"
•	Else → "Not Eligible".
'''

phy = int(input("Enter Physics marks: "))
chem = int(input("Enter Chemistry marks: "))
math = int(input("Enter Math marks: "))

total = phy + chem + math
avg = total / 3

print("Total Marks:", total)
print("Average:", avg)

if avg >= 70 and phy >= 60 and chem >= 60 and math >= 60:
    print("Eligible for Admission")
elif math >= 90:
    print("Eligible under Math Special Quota")
else:
    print("Not Eligible")
