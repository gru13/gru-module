from tern import *
win=Tk()
win.title("calculator")
win.geometry("300x400")
l1=Label(win,text="a")
l1.grid(column=0, row=0)
e1=Entry(win,width=3)
e1.grid(column=1, row=0)
l2= Label(win,text="b")
l2.grid(column=0, row=1)
e2=Entry(win,width=3)
e2.grid(column=1, row=1)
re=Label(win,text="result")
re.grid(column=0, row=2)
rel=Label(win,text="0")
rel.grid(column=1, row=2)
def a():
    A=int(e1.get())
    B=int(e2.get())
    r=A+B
    rel.config(text=r)
def s():
    A=int(e1.get())
    B=int(e2.get())
    r=A-B
    rel.config(text=r)
def m():
    A=int(e1.get())
    B=int(e2.get())
    r=A*B
    rel.config(text=r)
def d():
    A=int(e1.get())
    B=int(e2.get())
    r=A/B
    rel.config(text=r)
def c():
    win.destroy()
a=Button(win,text="add",command=a)
a.grid(column=2, row=0)

s=Button(win,text="sub",command=s)
s.grid(column=3, row=0)

m=Button(win,text="multiply",command=m)
m.grid(column=2, row=1)

d=Button(win,text="dvide",command=d)
d.grid(column=3, row=1)

close=Button(win,text="close",command=c)
close.grid(column=2, row=2)
win.mainloop()
