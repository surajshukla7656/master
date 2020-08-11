import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as errorwindow


win=tk.Tk()
win.title("CALCULATOR:CREATED BY SURAJ SHUKLA")
win.geometry("800x500")


# labelframe consisting buttons and entrybox 

main_frame=tk.LabelFrame(win,borderwidth=20,bg=random.choice(["red","blue","violet","brown","black","maroon"]))
main_frame.grid(row=0, column=0)


# entrybox for input and displaying of data
entry_value=tk.StringVar()
entry_main_=tk.Entry(main_frame,width=40,font=("calibri",20),borderwidth=10,textvariable=entry_value)
entry_main_.focus()
entry_main_.grid(row=1, columnspan=4,ipady=20)


# dict for generating button widgets 
nummeric_pad={
    "=":"button_eq_func(None)",
    "clear":"entry_main_.delete(0,\"end\")",
    "back":"back(None)",
    "0":0,
    "1":1,
    "+":"entry_main_.insert(tk.END,\"+\")",
    "2":2,
    "3":3,
    "-":"entry_main_.insert(tk.END,\"-\")",
    "4":4,
    "5":5,
    "*":"entry_main_.insert(tk.END,\"*\")",
    "6":6,
    "7":7,
    "/":"entry_main_.insert(tk.END,\"/\")",
    "8":8,
    "9":9,
    "functions":"function()"
    }   


# function performed by button_eq
def button_eq_func(event):
    input_data=entry_value.get()
    entry_main_.delete(0,"end")
    try:
        output_data=eval(input_data)
    except :
        #messagebox to showerror when entered invalid values for the calculation
        errorwindow.showerror("valueError","you have entered invalid input")
    
    else:
        entry_main_.insert(tk.END,output_data)
#binding enter key to the button_eq_func
entry_main_.bind("<Return>",button_eq_func)



# function to remove last entered value from the  main entrybox
def back(event):
    input_data=entry_value.get()
    entry_main_.delete(0,"end")
    entry_main_.insert(tk.END,input_data[:-1])
#binding backspace key to the func back
entry_main_.bind("BackSpace",back)


#constructor function for construction button widgets in main window(i.e win)
def button_constructor(contructor_dict,labelframe,row_count,column_count,column_control,*args):
    # row_count=20            #controls row position
    # column_count=1          #controls column position
    count=1                 #for intialization of column to 0
    for button,value in contructor_dict.items():
        #instances for button of nummeric pad containing func for input of data in entrybox

        if isinstance(value,int)==False:
            button_instance=tk.Button(labelframe, text=str(button),width=20,highlightbackground="black",font=50,activebackground="grey",bg="dark blue",borderwidth=10,foreground="red",command=lambda value=value:eval(value))
        
        else:
            button_instance=tk.Button(labelframe, text=str(button),width=20,highlightbackground="black",font=(50),activebackground="grey",bg="yellow",borderwidth=10,foreground="red",command=lambda value=value: entry_main_.insert(tk.END,value))
        
        button_instance.grid(row=row_count, column=column_count,padx=5,pady=5)
    
        column_count+=1
        count+=1
        if count==column_control:
            row_count+=1
            count=1
            column_count=1




button_constructor(nummeric_pad,main_frame,3,1,4)
    

win.mainloop()
