from tkinter import Label,Entry,Button,Tk,N

from tkinter.ttk import Combobox

win=Tk()
#~~~~~~~INITIAL THE WINDOW~~~~~~~~~
win.title("ABIRAMI SILKS")
win.config(bg="thistle")
win.geometry("1200x700")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Title:ABIRAMI SILKS
title=Label(text="ABIRAMI SILKS",font=("comforat",60),bg="lavender",fg="royal blue")
title.grid(sticky=N)
#Start  the body 


#function for label and entry
def hh(win,e,name,x,y,bc="white",fc="black",bd=None):
    wide=len(name)+5
    e=Entry(win,width=len(name)*10,bd=bd)

    b=Label(text=name,width=wide,bg=bc,fg=fc,bd=bd)
    b.grid(column=x,row=y)

    e.grid(column=x+1,row=y)
e="ll"
hh(win,e,"Name",20,20)


#START the Program
win.mainloop()
