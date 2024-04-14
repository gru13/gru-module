import tkinter  as k
import tkinter.ttk as kk
import random as r
from time import *

tk = k.Tk()
pht = k.PhotoImage(file="START.png")
o1 = k.PhotoImage(file="one.png")
o2 = k.PhotoImage(file="two.png")
o3 = k.PhotoImage(file="three.png")
o4 = k.PhotoImage(file="four.png")
o5 = k.PhotoImage(file="five.png")
o6 = k.PhotoImage(file="six.png")



def start():
    global la
    global o1
    global o2
    global o3
    global o4
    global o5
    global o6
    y=r.randint(1,7)
    if y == 1:
        la.config(image=o1)
    elif y == 2:
        la.config(image=o2)
    elif y == 3:
        la.config(image=o3)
    elif y == 4:
        la.config(image=o4)
    elif y == 5:
        la.config(image=o5)
    elif y == 6:
        la.config(image=o6)

la= kk.Button(tk,image=pht,command=start)
la.grid(row=1)

tk.title("Dices")
tk.mainloop()

