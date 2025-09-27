'''
Online Food Delivery Charges
Inputs: distance, order_amount, user_type (Normal, Gold, Platinum).
Rules:
•	Base delivery = ₹50
•	If distance > 5 km → +₹10/km extra
•	Free delivery if order_amount ≥ 1000
•	Membership benefits:
o	Gold → 20% discount on order
o	Platinum → 30% discount on order
o	Normal → No discount
Display final bill amount including delivery.
'''

dist = float(input("Enter distance (km): "))
amt = float(input("Enter order amount: "))
utype = input("User type (Normal/Gold/Platinum): ").lower()

delivery = 50
if dist > 5:
    delivery += (dist - 5) * 10

if amt >= 1000:
    delivery = 0

disc = 0
if utype == "gold":
    disc = 0.2 * amt
elif utype == "platinum":
    disc = 0.3 * amt

final = amt - disc + delivery

print("Final Bill Amount = ₹", final)
