import GUI_Data
import pandas as pd
from tkinter import *
import face_storing
import utilities

def user():

    emp_id = GUI_Data.gui_storing()

    if emp_id == 1:
        face_storing.face_storing(emp_id)
        exit()

    df1 = pd.read_excel("Data_of_Employees.xlsx", engine='openpyxl')
    admin_number = df1.iloc[0]['Phone_Number']

    def function():
        #global emp_id, admin_number
        admin = admin_name.get()
        master.destroy()
        utilities.whatsApp_user_details(emp_id, admin)

    master = Tk()
    master.configure(background='light green')
    master.geometry("500x300")
    master.title("Admin Name")
    Label(master, text="Please Enter how Admin number {} is stored in your WhatsApp".format(admin_number),
          bg="light green", font='arial 15 bold').grid(row=0, column=0)

    admin_name = Entry(master)
    admin_name.grid(row=1, column=0)

    Button(master, text="Next >", command=function).grid(row=2, column=0)
    master.mainloop()

    return emp_id
