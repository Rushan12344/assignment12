import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    name=name_var.get()
    password=passw_var.get()
    #print("The name is:" + name)
    #print("The password is : " + password)
    name_print=tk.Label(root,text="Your name is :"+name,font=('Arial',10,'bold')).pack()
    pass_print=tk.Label(root,text="Your password is :"+password,font=('Arial',10,'bold')).pack()
    
    name_var.set("")
    passw_var.set("")

name_label=tk.Label(root,text='Username',font=('Arial',10,'bold')).pack()
name_entry=tk.Entry(root,textvariable=name_var,font=('Arial',10,'normal')).pack()
passw_label=tk.Label(root,text='Password',font=('Arial',10,'bold')).pack()
passw_entry=tk.Entry(root,textvariable=passw_var,font=('Arial',10,'normal'),show='*').pack()
sub_btn=tk.Button(root,text='Submit',command=submit).pack()

root.mainloop()