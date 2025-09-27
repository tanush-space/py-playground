'''Q1. Employee Salary Slip Generator
Write a program that accepts basic salary of an employee and calculate the following:
•	HRA = 20% of basic
•	DA = 10% of basic
•	PF = 12% of basic
•	Gross Salary = Basic + HRA + DA
•	Net Salary = Gross – PF
Decision Rules:
•	If Net Salary ≥ 80,000 → Category = "High Earner"
•	If 50,000 ≤ Net Salary < 80,000 → "Mid Earner"
•	Else → "Low Earner"
'''


basic = float(input("Enter basic salary: "))

hra = 0.2 * basic
da = 0.1 * basic
pf = 0.12 * basic

gross = basic + hra + da
net = gross - pf

if net >= 80000:
    cat = "High Earner"
elif net >= 50000:
    cat = "Mid Earner"
else:
    cat = "Low Earner"

print("\n--- Salary Slip ---")
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("PF:", pf)
print("Gross Salary:", gross)
print("Net Salary:", net)
print("Category:", cat)
