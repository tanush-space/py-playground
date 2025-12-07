import random
import string

print("Hangman")
ws = ["python","stream","variable","object","function","module","laptop","coffee","planet","garden","travel","winter","summer","school","puzzle"]
w = random.choice(ws)
l = 6
u = set()
a = set(string.ascii_lowercase)
need = set(w)

while len(need) > 0 and l > 0:
    show = " ".join([ch if ch in u else "_" for ch in w])
    print(f"\nword: {show}   lives: {l}   used: {' '.join(sorted(u))}")
    g = input("letter: ").lower().strip()

    if len(g) != 1 or g not in a:
        print("type one letter")
        continue
    if g in u:
        print("already tried")
        continue

    u.add(g)
    if g in need:
        need.remove(g)
        print("good")
    else:
        l -= 1
        print("nope")

if l == 0:
    print(f"\nyou lost, word was: {w}")
else:
    print(f"\nyou win! word: {w}")
