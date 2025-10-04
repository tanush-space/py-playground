from tkinter import *
import math

def click(btn):
    try:
        if btn == "=":
            result = str(eval(screen_var.get()))
            screen_var.set(result)
        elif btn == "C":
            screen_var.set("")
        elif btn == "√":
            result = str(math.sqrt(float(screen_var.get())))
            screen_var.set(result)
        elif btn == "!":
            n = int(screen_var.get())
            result = str(math.factorial(n))
            screen_var.set(result)
        elif btn == "%":
            result = str(float(screen_var.get())/100)
            screen_var.set(result)
        else:
            screen_var.set(screen_var.get() + btn)
    except:
        screen_var.set("Error")

root = Tk()
root.title("Ultimate Student Calculator")
root.geometry("400x600")
root.configure(bg="#f8f1f1")

screen_var = StringVar()
screen = Entry(root, textvar=screen_var, font=("Helvetica", 24), bd=5, relief=RIDGE, justify=RIGHT, bg="#fff", fg="#333")
screen.pack(fill=X, padx=20, pady=20, ipady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "√", "!", "%"]
]

colors = {
    "num": "#ffffff",
    "op": "#ffb347",
    "special": "#90ee90"
}

for r in buttons:
    frame = Frame(root, bg="#f8f1f1")
    frame.pack(expand=True, fill=BOTH, padx=10, pady=5)
    for b in r:
        if b in ["+", "-", "*", "/", "="]:
            bgc = colors["op"]
        elif b in ["C", "√", "!", "%"]:
            bgc = colors["special"]
        else:
            bgc = colors["num"]
        Button(frame, text=b, font=("Helvetica", 20), bd=0, bg=bgc, fg="#333", activebackground="#ddd",
               relief=RAISED, command=lambda x=b: click(x)).pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

root.mainloop()
 