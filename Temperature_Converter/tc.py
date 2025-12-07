def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

def convert(v, f, t):
    if f == t:
        return v
    if f == "c":
        if t == "f": return c_to_f(v)
        if t == "k": return c_to_k(v)
    if f == "f":
        if t == "c": return f_to_c(v)
        if t == "k": return f_to_k(v)
    if f == "k":
        if t == "c": return k_to_c(v)
        if t == "f": return k_to_f(v)

while True:
    print("\nTemperature Converter")
    print("type 'q' anytime to quit")
    try:
        v = input("Enter value: ").strip()
        if v.lower() == "q":
            print("bye!")
            break
        v = float(v)
        f = input("From (C/F/K): ").lower()
        if f == "q": break
        t = input("To (C/F/K): ").lower()
        if t == "q": break

        if f not in ["c","f","k"] or t not in ["c","f","k"]:
            print("invalid unit")
            continue

        res = convert(v, f, t)
        print(f"{v}°{f.upper()} = {round(res, 2)}°{t.upper()}")

    except ValueError:
        print("enter number only")
