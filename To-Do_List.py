from cgitb import text
import tkinter
from tkinter import ttk
from tkinter import messagebox
import random

#Window Settings and Window Creation
window = tkinter.Tk()
window.configure(bg="purple")
window.title("To-Do List")
window.geometry("275x275")


#Sample Task List
tasks =[]

#Functions
def update_listbox():
    clear_listbox()
    
    for task in tasks:
        lbl_tasks.insert("end", task)

def clear_listbox():
    lbl_tasks.delete(0, "end")

def add_task():
    #get user input
    task = txt_input.get()
    #ensure user has entered a task
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Note!", "Please enter a task")
    #clear the textbox
    txt_input.delete(0, "end")

def delete_task():
    #Get the txt of the selected item
    task = lbl_tasks.get("active")
    #confirm task is in tasks
    if task in tasks:
        ##returns a boolean
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete task: {}?".format(task))
        if confirm:
            tasks.remove(task)
    #update task list
    update_listbox()

def sort_list():
    tasks.sort()
    update_listbox()



def delete_all(event):
    global tasks
    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete task?")
    if confirm:
        tasks = []
        update_listbox()

def show_listbox():
    global tasks
    for task in tasks:
        lbl_tasks.insert("end", task)


#window.bind('<Return>', add_task)#Allows the user to enter a task without hitting the add task button. Maps the enter key to the add task button
#window.bind('<Delete>', delete_all)

##Creating lbls and buttons
lbl_title = tkinter.Label(window, text="To-Do List", bg="purple")
lbl_title.grid(row = 0, column=1)

lbl_display = tkinter.Label(window, text="", bg="purple")
lbl_display.grid(row=1, column=0)

txt_input = tkinter.Entry(window, width=15)
txt_input.grid(row=1, column=1)

btn_add_task = tkinter.Button(window, text="Add Task", fg="grey", bg="black", command=add_task)
btn_add_task.grid(row=1, column=0)

btn_delete_task = tkinter.Button(window, text="Delete Task", fg="grey", bg="black", command=delete_task)
btn_delete_task.grid(row=1, column=3)

btn_dAll_task = tkinter.Button(window, text="Delete All", fg="grey", bg="Black", command=delete_all)
btn_dAll_task.grid(row=2, column=3)

btn_sort_task = tkinter.Button(window, text="Sort", fg="grey", bg="Black", command=sort_list)
btn_sort_task.grid(row= 2, column=0)

lbl_tasks = tkinter.Listbox(window)
lbl_tasks.grid(row=2, column=1, rowspan=5)

show_listbox()
window.mainloop()