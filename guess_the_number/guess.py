import random

print("Guess the Number")
low = 1
high = 100
n = random.randint(low, high)
c = 0

while True:
    s = input(f"Pick a number {low}-{high}: ")
    try:
        g = int(s)
    except:
        print("enter a number")
        continue
    c += 1
    if g < n:
        print("too small")
    elif g > n:
        print("too big")
    else:
        print(f"you got it in {c} tries")
        break
