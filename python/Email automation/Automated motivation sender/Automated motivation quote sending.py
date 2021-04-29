import smtplib
import datetime as dt
import random



my_email="redwan.ahmed1512039@gmail.com"
password="Redwan(1)"

now=dt.datetime.now()
weekday=now.weekday()


if weekday==1:
    with open("quotes.txt",encoding="utf8") as file:  # decoding utf-8 object/byte object to unicode object
        quotes=file.readlines()
        quote=random.choice(quotes)
        
        message="Subject:Monday Motivation\n\n"+quote
        
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
        from_addr=my_email,
        to_addrs="rootovermahmud@gmail.com",
        msg=message.encode(encoding="utf8")  # encoding python object/unicode object to byte object/utf-8 object
        )
        
        






