'''Online Examination Result
Inputs: Correct answers, Wrong answers, Unattempted.
Marking scheme: +4 for correct, –1 for wrong, 0 for unattempted.
Rules:
•	Score ≥ 180 → "Excellent"
•	120–179 → "Good"
•	60–119 → "Average"
•	Below 60 → "Fail"
Also, if Wrong answers > Correct answers, show: "Improve accuracy!"
'''

corr = int(input("Enter correct answers: "))
wrong = int(input("Enter wrong answers: "))
unatt = int(input("Enter unattempted: "))

score = corr * 4 + wrong * -1

print("Total Score:", score)

if score >= 180:
    print("Excellent")
elif score >= 120:
    print("Good")
elif score >= 60:
    print("Average")
else:
    print("Fail")

if wrong > corr:
    print("Improve accuracy!")
