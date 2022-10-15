from tkinter import*
import tkinter
root = Tk()
logo = tkinter.PhotoImage(file="PNG_transparency_demonstration_1.png")
w1=Label(root,image=logo).pack(side="right")
msg="Welcome semester 3"
W2=Label(root,justify=tkinter.LEFT,padx=10,text=msg).pack(side="left")
root.mainloop()
