import pandas as pd
import User
import face_storing
import utilities
from tkinter import *

def function():
    otp = otp_received.get()
    if int(otp_sent) == int(otp):
        root.destroy()
        face_storing.face_storing(emp_id)
    else:
        root.destroy()
        master=Tk()
        Label(master,text='Invalid OTP, try again',font='arial 15 bold').grid(row=0,column=0)


emp_id = User.user()

otp_sent = utilities.otp_generator()
df1 = pd.read_excel("Data_of_Employees.xlsx", engine='openpyxl') # df1.series['Name'] = column --> tolist == name
admin_number = df1.iloc[0]['Phone_Number']
root = Tk()
root.configure(background='light green')
root.geometry("500x300")
root.title("OTP")
Label(root, text="Please Enter the OTP SENT to Admin number {}".format(admin_number),
      bg="light green", font='arial 15 bold').grid(row=0, column=0)

otp_received = Entry(root)
otp_received.grid(row=1, column=0)
Button(root, text="Submit", command=function).grid(row=2, column=0)
root.mainloop()