'''BMI calculator'''
Weight = int(input("Enter your weight in kg: "))
Height = float(input("Enter your height in meters: "))
BMI = Weight / (Height ** 2)
print("Your BMI is: " + str(int(BMI)))