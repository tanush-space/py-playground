'''Loan Eligibility System
Create a program that checks loan eligibility.
Inputs: age, monthly_income, existing_loan, CIBIL_score.
Conditions:
•	Age must be between 21–60
•	Income must be ≥ 25,000
•	Existing loan must be ≤ 50% of income
•	CIBIL score ≥ 700
If all conditions are satisfied → "Eligible for Loan"
Else, display reason for rejection (e.g., "Rejected due to low CIBIL score").
'''

age = int(input("Enter age: "))
inc = float(input("Enter monthly income: "))
loan = float(input("Enter existing loan amount: "))
cibil = int(input("Enter CIBIL score: "))

if age < 21 or age > 60:
    print("Rejected due to age limit")
elif inc < 25000:
    print("Rejected due to low income")
elif loan > 0.5 * inc:
    print("Rejected due to high existing loan")
elif cibil < 700:
    print("Rejected due to low CIBIL score")
else:
    print("Eligible for Loan")
