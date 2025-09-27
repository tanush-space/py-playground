'''Smart Traffic Fine System
A city wants to implement a traffic fine system.
Inputs: speed, vehicle_type (car/bike/truck), seat_belt (Yes/No), helmet (Yes/No if bike).
Rules:
•	Speed > 80 → Fine ₹2000
•	Car without seat belt → +₹1000 fine
•	Bike without helmet → +₹1500 fine
•	Truck speed > 60 → +₹3000 fine
Display: "Total Fine = …"
If no rules violated → "No Fine. Drive Safe 🚗".
'''


spd = int(input("Enter speed: "))
vtype = input("Enter vehicle type (car/bike/truck): ").lower()
belt = input("Seat belt (Yes/No): ").lower()
helm = "yes"
if vtype == "bike":
    helm = input("Helmet (Yes/No): ").lower()

fine = 0

if spd > 80:
    fine += 2000
if vtype == "car" and belt == "no":
    fine += 1000
if vtype == "bike" and helm == "no":
    fine += 1500
if vtype == "truck" and spd > 60:
    fine += 3000

if fine == 0:
    print("No Fine. Drive Safe 🚗")
else:
    print("Total Fine = ₹", fine)
