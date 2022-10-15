from tkinter import*
root=Tk() 
root.geometry("300x200")
W=Label(root,text='Gujarat University',font="50").pack()
Checkbutton1=IntVar()
Checkbutton2=IntVar()
Checkbutton3=IntVar()


def submit():
    c1=Checkbutton1.get()
    c2=Checkbutton2.get()
    c3=Checkbutton3.get()
    if(c1==1):
            print1=Label(root,text="Tutorial",font=('Arial',10,'bold')).pack()
    if(c2==1):
            print2=Label(root,text="Courses",font=('Arial',10,'bold')).pack()
    if(c3==1):
            print3=Label(root,text="Student",font=('Arial',10,'bold')).pack()

    
Button1=Checkbutton(root,text="Tutorial",variable=Checkbutton1,onvalue=1,offvalue=0,height=2,width=10).pack()
Button2=Checkbutton(root,text="Courses",variable=Checkbutton2,onvalue=1,offvalue=0,height=2,width=10).pack()
Button3=Checkbutton(root,text="Student",variable=Checkbutton3,onvalue=1,offvalue=0,height=2,width=10).pack()
sub_btn=Button(root,text='Submit',command=submit).pack()


root.mainloop()