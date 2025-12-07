import random

print("Rock Paper Scissors Game")
opt = ["rock", "paper", "scissors"]

while True:
    user = input("choose rock, paper or scissors: ").lower()
    if user not in opt:
        print("invalid choice")
        continue

    comp = random.choice(opt)
    print("computer chose:", comp)

    if user == comp:
        print("it's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("you win!")
    else:
        print("you lose!")

    again = input("play again? (y/n): ").lower()
    if again != "y":
        print("bye!")
        break
