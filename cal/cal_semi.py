from tern import *
from tkinter.ttk import Combobox
import math
a,b=0,1
def clear ():
    global d
    d=str()
    la.config(text=d)
def log ():
   global d
   global t
   global v
   global l
   if v!=0:
    l+=1
   v+=1
   u=math.log10(float(d))
   u=round(u,4)
   la.config(text=u)
   p = str(v) + ")" + "log(" + str(d) + ")" + "=" + str(u)
   i = list(t)
   i.append(p)
   t=tuple(i)
   his.configure(values=t)
   his.current(l)
   d=str()
def root ():
   global d
   global t
   global v
   global l
   if v!=0:
    l+=1
   v+=1
   u=float(d)**(1/2)
   la.config(text=u)
   p = str(v) + ")" +str(d)+"="+str(u)
   i = list(t)
   i.append(p)
   t=tuple(i)
   his.configure(values=t)
   his.current(l)
   d=str()
def roo ():
   global d
   global t
   global v
   global l
   if v!=0:
    l+=1
   v+=1
   u=float(d)**(1/3)
   la.config(text=u)
   p = str(v) + ")" +str(d)+"="+str(u)
   i = list(t)
   i.append(p)
   t=tuple(i)
   his.configure(values=t)
   his.current(l)
   d=str()
def antilog ():
   global d
   global t
   global v
   global l
   if v!=0:
    l+=1
   v+=1
   e=eval(d)
   if e < -4 :
       print("in")
       o = chk_type(e)
       u =math.e+o
   else:
    o=chk_type(e)
    u=10**o
   u=round(u,4)
   la.config(text=u)
   p=str(v)+") "+"antilog("+str(d)+")"+"="+str(u)
   i = list(t)
   i.append(p)
   t=tuple(i)
   his.configure(values=t)
   his.current(l)
   d=str()
def one ():
   global d
   d=d+"1"
   la.config(text=d)
def two ():
   global d
   d=d+"2"
   la.config(text=d)
def three ():
   global d
   d=d+"3"
   la.config(text=d)
def four():
   global d
   d=d+"4"
   la.config(text=d)
def five ():
   global d
   d=d+"5"
   la.config(text=d)
def six ():
   global d
   d=d+"6"
   la.config(text=d)
def seven ():
   global d
   d=d+"7"
   la.config(text=d)
def eight ():
   global d
   d=d+"8"
   la.config(text=d)
def nine ():
   global d
   d=d+"9"
   la.config(text=d)
def zeo ():
   global d
   d=d+"0"
   la.config(text=d)
def plus():
   global d
   d=d+"+"
   la.config(text=d)
def dot():
   global d
   d=d+"."
   la.config(text=d)
def minus ():
   global d
   d=d+"-"
   la.config(text=d)
def multi ():
   global d
   d=d+"*"
   la.config(text=d)
def close():
    win.destroy()
def divi ():
   global d
   d=d+"/"
   la.config(text=d)
def res ():
   global d
   global t
   global v
   global l
   if v!=0:
    l+=1
   v+=1
   u=eval(d)
   la.config(text=u)
   p=str(v)+")"+d+"="+str(u)
   i = list(t)
   i.append(p)
   t=tuple(i)
   his.configure(values=t)
   his.current(l)
   d=str()
win=Tk()
v=0
l=0
gui.creat_win(win,tle="calculator",winsize="550x200",bgcol="grey")
la=Label(win,text="0",bd=5,bg="blue",fg="black",width=10)
la.grid(column=1, row=0)
d=str()
t=()
his=Combobox(win,value=t)
 #set the selected item
his.grid(column=3, row=8)
Label(win,text="HISTORY").place(y=180, x=185)
one=gui.bton(win,0,1,btn="1",btcol="green",fcol="black",c=one)
two=gui.bton(win,1,1,btn="2",btcol="green",fcol="black",c=two)
three=gui.bton(win,2,1,btn="3",btcol="green",fcol="black",c=three)
four=gui.bton(win,0,2,btn="4",btcol="green",fcol="black",c=four)
five=gui.bton(win,1,2,btn="5",btcol="green",fcol="black",c=five)
six=gui.bton(win,2,2,btn="6",btcol="green",fcol="black",c=six)
seven=gui.bton(win,0,3,btn="7",btcol="green",fcol="black",c=seven)
eight=gui.bton(win,1,3,btn="8",btcol="green",fcol="black",c=eight)
nine=gui.bton(win,2,3,btn="9",btcol="green",fcol="black",c=nine)
zero=gui.bton(win,1,4,btn="0",btcol="green",fcol="black",c=zeo)
plus=gui.bton(win,3,1,btn="+",fcol="black",c=plus)
minus=gui.bton(win,3,2,btn="-",fcol="black",c=minus)
multi=gui.bton(win,3,3,btn="*",fcol="black",c=multi)
rot=gui.bton(win,3,6,btn="sq-root",fcol="black",c=root)
rt=gui.bton(win,4,6,btn="cube-root",fcol="black",c=roo)
divi=gui.bton(win,3,4,btn="/",fcol="black",c=divi)
res=gui.bton(win,4,2,btn="result",btcol="green",fcol="black",c=res)
close=gui.bton(win,4,3,btn="close",btcol="green",fcol="black",c=close)
Float=gui.bton(win,4,4,btn=".",btcol="white",fcol="black",c=dot)
log=gui.bton(win,4,5,btn="log",btcol="white",fcol="black",c=log)
antilog=gui.bton(win,3,5,btn="antilog",btcol="white",fcol="black",c=antilog)
clear=gui.bton(win,4,1,btn="clear",fcol="black",c=clear)
win.mainloop()
