'''E-Commerce Discount Calculator
Write a program that asks for product price and user type (Regular, Premium, VIP).
Discount Rules:
•	Regular:
o	< 500 → 5%
o	≥ 500 → 10%
•	Premium:
o	< 1000 → 15%
o	≥ 1000 → 20%
•	VIP: Flat 25% discount always
Also apply extra 5% discount if payment mode = "Online".
Finally display the discounted price.
'''
price = float(input("Enter product price: "))
utype = input("Enter user type (Regular/Premium/VIP): ").lower()
pay = input("Payment mode (Online/Offline): ").lower()

disc = 0

if utype == "regular":
    if price < 500:
        disc = 0.05 * price
    else:
        disc = 0.10 * price
elif utype == "premium":
    if price < 1000:
        disc = 0.15 * price
    else:
        disc = 0.20 * price
elif utype == "vip":
    disc = 0.25 * price

if pay == "online":
    disc += 0.05 * price

final = price - disc
print("Discounted Price = ₹", final)
