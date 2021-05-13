import pandas as pd
import random
from tkinter import *

from selenium import webdriver
from twilio.rest import Client

def otp_generator(): # OTP GENERATOR

    df1 = pd.read_excel('Data_of_Employees.xlsx', engine='openpyxl')

    twilio_ssid = df1.iloc[0]['Twilio_SSID']
    twilio_token = df1.iloc[0]['Twilio_Token']
    twilio_no = '+' + str(int(df1.iloc[0]['Twilio_Number']))
    admin_number = '+'+str(df1.iloc[0]['Phone_Number'])

    OTP = random.randint(1000, 9999)  # GENERATED OTP BETWEEN THESE NUMBERS
    client = Client(twilio_ssid, twilio_token) #ssid,token
    client.messages.create(to=[admin_number], from_=twilio_no, body=OTP)

    return OTP

def whatsApp_user_details(emp_id,admin): # VERIFICATION DETAILS REQUEST FROM USER

    df1 = pd.read_excel('Data_of_Employees.xlsx', engine='openpyxl')
    name = df1.iloc[emp_id-1]['Name']
    phone_no = df1.iloc[emp_id-1]['Phone_Number']

    def function():
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(admin))
        user.click()
        textbox = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        textbox.send_keys("Name : {}\nEmployee ID : {}\nPhone Number : {}\nPlease process my request of adding new facial biometric"
                          .format(name,emp_id,phone_no))
        button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
        button.click()

        master.destroy()

    driver = webdriver.Chrome("chromedriver")
    driver.get("https://web.whatsapp.com/")

    master = Tk()
    master.configure(background='light green')
    master.geometry("500x300")
    master.title("Admin Name")
    Label(master, text="Press Enter after scanning WhatsApp Web",
          bg="light green", font='arial 15 bold').grid(row=0, column=0)

    Button(master, text="Next >", command=function).grid(row=2, column=0)
    master.mainloop()

if __name__ == '__main__':
    pass





