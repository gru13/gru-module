
from tkinter import Label,Entry,Button,Tk,N

from tkinter.ttk import Combobox

win=Tk()
#~~~~~~~INITIAL THE WINDOW~~~~~~~~~
win.title("ABIRAMI SILKS")
win.config(bg="thistle")

def hh(win,name,x,y,bc="white",fc="black",bd=None):
    wide=len(name)+5
    e=Entry(win,width=len(name)*10,bd=bd)

    b=Label(text=name,width=wide,bg=bc,fg=fc,bd=bd)
    b.grid(column=x,row=y)

    e.grid(column=x+1,row=y)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hh(win,"10",2,0,bc="grey",fc="white",bd=10)
hh(win,"10",2,1,bc="grey",fc="white",bd=10)
hh(win,"10",0,0,bc="grey",fc="white",bd=10)
win.mainloop()
