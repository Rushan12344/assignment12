import tkinter as tk
from tkinter import*
root=Tk()
root.geometry("500x500")
listSample=Listbox(root,width=70,height=30,fg="red",font=("Arial 28"))
listSample.insert(1,"Pizza")
listSample.insert(2,"Pizza 1")
listSample.insert(3,"Pizza 3")

listSample.pack()
root.mainloop()

