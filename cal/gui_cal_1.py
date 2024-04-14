from tern import *
win=Tk()
gui.creat_win(win,tle="calculator",winsize="450x200",bgcol="grey")
la=Label(win,text="0",width=15,bg="blue",fg="black")
la.grid(column=1, row=0)
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
   d=eval(d)
   la.config(text=d)
   d=str()
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
divi=gui.bton(win,3,4,btn="/",fcol="black",c=divi)
res=gui.bton(win,4,2,btn="result",btcol="green",fcol="black",c=res)
close=gui.bton(win,4,3,btn="close",btcol="green",fcol="black",c=close)
win.mainloop()
