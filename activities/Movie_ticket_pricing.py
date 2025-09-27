'''Movie Ticket Pricing System
Inputs: age, movie_type (2D/3D), day (weekday/weekend).
Rules:
•	Base price = ₹200
•	If 3D → +₹100
•	Weekend → +₹50
•	Age < 12 → 50% discount
•	Age > 60 → 30% discount
Calculate and display final ticket price
'''

age = int(input("Enter age: "))
mtype = input("Movie type (2D/3D): ").lower()
day = input("Day (weekday/weekend): ").lower()

price = 200

if mtype == "3d":
    price += 100
if day == "weekend":
    price += 50

if age < 12:
    price *= 0.5
elif age > 60:
    price *= 0.7

print("Final Ticket Price = ₹", price)
