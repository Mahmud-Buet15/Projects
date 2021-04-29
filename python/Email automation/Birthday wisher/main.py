import smtplib
import datetime as dt
import pandas as pd
import random

#randomly selecting a letter to send
# text_options=["letter_1.txt","letter_2.txt","letter_3.txt"]
# letter=random.choice(text_options)

letter=f"letter_templates/letter_{random.randint(1,3)}.txt"

#the mail id which will be used to send message
my_email="redwan.ahmed1512039@gmail.com"
password="Redwan(1)"


#reading file from csv which holds information about person and then converting it to a dictionary 
df=pd.read_csv("birthdays.csv")
birthdays=df.to_dict("index")


#finding the current date and matching it with the data from csv
now=dt.datetime.now()
month=now.month
day=now.day 

for i in range(len(birthdays)):
    if birthdays[i]["month"]==month and  birthdays[i]["day"]==day:
        mail_id=birthdays[i]["email"]
        name=birthdays[i]["name"]
        
        with open(letter) as file:
            text=file.read()
            text=text.replace("[NAME]",name)
        
        message=f"Subject: Birthday wish\n\n{text}"  #f"something{value}"  value can be any variable if we use f .otherwise it will be raw text  
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=mail_id,
                msg=message.encode('utf-8')  # coverting a python object/unicode object to byte object/utf-8 object 
                )