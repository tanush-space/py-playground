'''wap to find out how many day, weeks and months we have left if we live until 90 years old
input : your correct age
output : you have a days, b weeks, c months left
1 year = 365 days
1 year = 52 weeks
1 year = 12 months
'''
age = int(input("Enter your current age: "))    
years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
