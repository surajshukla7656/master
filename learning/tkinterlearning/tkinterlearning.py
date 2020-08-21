#------------------------------starter code----------------------------->>>>

import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("GUI")



#-----------------------------create labels------------------------------>>>>

# ttk.Label(win,text="Enter your name:").pack()
name_label=ttk.Label(win,text="Enter your name:")
name_label.grid(row=0,column=0,sticky=tk.W)


age_label=ttk.Label(win,text="Enter your age:")
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(win,text="Enter your email :")
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text="Enter your gender :")
gender_label.grid(row=4,column=0,sticky=tk.W)

#-------------------------create entery box------------------------->>
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=12,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=12,textvariable=age_var)
age_entrybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=12,textvariable=email_var)
email_entrybox.grid(row=2,column=1)

#----------------------------create combobox--------------------------------->>>

gender_var=tk.StringVar()

gender_combobox=ttk.Combobox(win,width=11,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("male","female","others")
gender_combobox.current(0)
gender_combobox.grid(row=4,column=1)

#-----------------------------radiobutton------------------>>

usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text="student",value="student",variable=usertype)
radiobtn1.grid(row=5,column=0)

radiobtn2=ttk.Radiobutton(win,text="teacher",value="teacher",variable=usertype)
radiobtn2.grid(row=5,column=1)

#-----------------------checkbutton------------------->>
Checkbutton=tk.IntVar()
cb=ttk.Checkbutton(win,text="check if you  want to subscrive to our newletter",variable=Checkbutton)

cb.grid(row=6,columnspan=3)
#-------------------------------button----------------->>
def action():
    username=name_var.get()
    userage=age_var.get()
    useremail=email_var.get()
    print(f"{username} is {userage} years old, {useremail}")

    with open("file.txt","a") as f:
        f.write(f'{username},{userage},{useremail},{gender_var.get()},{usertype.get()},{Checkbutton.get()}')


    with open("file.txt","a") as f:
        from csv import DictWriter
        csv_writer=DictWriter(f,fieldnames=["username","useremail","gender","usertype","checkin"])
        # if os.stat("file.txt").st_size==0:
        csv_writer.writeheader()
        csv_writer.writerow=({
            "username":username,
            "useremail":useremail,
            "gender":gender_var.get(),
            "usertype":usertype,
            "checkin":Checkbutton.get(), 
            "newline":"\n"
        })


    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)


name_entrybox.configure(foreground="red")



submit_button=ttk.Button(win,text="submit",command=action)
submit_button.grid(row=7,column=1)




win.mainloop()
