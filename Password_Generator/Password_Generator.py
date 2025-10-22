import random
import string

# Password length
n = int(input("Enter password length: "))

# Characters to use
chars = string.ascii_letters + string.digits + string.punctuation

# Generate password
pwd = "".join(random.choice(chars) for _ in range(n))

print("Your secure password is:", pwd)
