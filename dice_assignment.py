import tkinter
from tkinter import*
import random

d=Tk()
d.geometry("800x550")
d1=tkinter.PhotoImage(file="1.png")
d2=tkinter.PhotoImage(file="2.png")
d3=tkinter.PhotoImage(file="3.png")
d4=tkinter.PhotoImage(file="4.png")
d5=tkinter.PhotoImage(file="5.png")
d6=tkinter.PhotoImage(file="6.png")

def roll():
    dice=[d1,d2,d3,d4,d5,d6]
    side=random.choice(dice)
    label=Label(d,image=side)
    label.place(x=230,y=50)
button=Button(d,text="Roll",width=40,height=5,font=10,bg="white",bd=2,command=roll)
button.place(x=150,y=300)

d.mainloop()