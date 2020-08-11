import tkinter as tk

from tkinter import ttk
win=tk.Tk()
win.title("labelframe")

label_frame=ttk.LabelFrame(win,text="Enter your details:")
label_frame.grid(row=0,column=0)
labels = ['What is your name : ' , 'What is your age ', 'What is your gender : ', 'Country : ', 'State : ', 'City : ', 'address']



for i in range(len(labels)):
    cur_label = 'label' + str(i) # label0, label1
    cur_label = ttk.Label(label_frame, text = labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W,padx=22,pady=5)

# entry box
name_var = tk.StringVar() 
user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'address' : tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox = 'entry' + i # entryname # entryage
    cur_entrybox = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    cur_entrybox.grid(column=1, row=counter)
    counter += 1 

def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())

submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=7, columnspan=2)

# name_entry = ttk.Entry(win, width=16, textvariable=name_var)
# name_entry.grid(row=0, column=1)


win.mainloop()