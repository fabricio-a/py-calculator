from tkinter import *
from functools import partial

calc = Tk()
calc.geometry("160x180")
calc["bg"] = "blue"

class sum:
    pass

s = sum()

def bot(bt):
    lb["text"] = lb["text"]+bt["text"]

def bot1(bt):
    s.p1 = int(lb["text"])
    lb["text"] = ""
    s.p=bt["text"]

def bot2():
    s.p2 = int(lb["text"])
    if s.p == "+":
        lb["text"] = str(s.p1+s.p2)
    elif s.p == "-":
        lb["text"] = str(s.p1-s.p2)
    elif s.p == "*":
        lb["text"] = str(s.p1*s.p2)
    elif s.p == "/":
        lb["text"] = str(s.p1/s.p2)

def bot3():
    lb["text"] = ""

lb1 = Label(calc,text="",bg = "blue")
lb1.grid(row=0,column=0)

lb = Label(calc,text="",bg = "blue")
lb.grid(row=1,column=0)

bt1 = Button(calc,text="1")
bt1.grid(row=2,column=0)
bt1["command"]=partial(bot,bt1)
bt2 = Button(calc,text="2")
bt2.grid(row=2,column=1)
bt2["command"]=partial(bot,bt2)
bt3 = Button(calc,text="3")
bt3.grid(row=2,column=2)
bt3["command"]=partial(bot,bt3)
bt4 = Button(calc,text="4")
bt4.grid(row=3,column=0)
bt4["command"]=partial(bot,bt4)
bt5 = Button(calc,text="5")
bt5.grid(row=3,column=1)
bt5["command"]=partial(bot,bt5)
bt6 = Button(calc,text="6")
bt6.grid(row=3,column=2)
bt6["command"]=partial(bot,bt6)
bt7 = Button(calc,text="7")
bt7.grid(row=4,column=0)
bt7["command"]=partial(bot,bt7)
bt8 = Button(calc,text="8")
bt8.grid(row=4,column=1)
bt8["command"]=partial(bot,bt8)
bt9 = Button(calc,text="9")
bt9.grid(row=4,column=2)
bt9["command"]=partial(bot,bt9)
btc = Button(calc,text="C",command=bot3)
btc.grid(row=5,column=0)
bt0 = Button(calc,text="0")
bt0.grid(row=5,column=1)
bt0["command"]=partial(bot,bt0)
btx = Button(calc,text="=",command=bot2)
btx.grid(row=5,column=2)

btm = Button(calc,text="+")
btm.grid(row=2,column=3)
btm["command"]=partial(bot1,btm)
btn = Button(calc,text="-")
btn.grid(row=3,column=3)
btn["command"]=partial(bot1,btn)
btp = Button(calc,text="*")
btp.grid(row=4,column=3)
btp["command"]=partial(bot1,btp)
btz = Button(calc,text="/")
btz.grid(row=5,column=3)
btz["command"]=partial(bot1,btz)

calc.mainloop()
