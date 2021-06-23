from tkinter import *
import tkinter as tk

top = Tk()

refcode = tk.StringVar()
def correct(inp):
    if inp.isdigit():
        enterednumber = inp
        ch = enterednumber[0]

        length = len(enterednumber)

        if (ch == "0"):
            return False
        else:
            if (length<=5):

                return True

            else:
                return False
    elif inp is "":

        return True
    else:
        return False

e = Entry(top,textvariable=refcode)
e.place(x = 50, y = 50)
reg = top.register(correct)
e.config(validate="key", validatecommand=(reg, "%P"))

R=refcode.get()
print(R)
top.mainloop()