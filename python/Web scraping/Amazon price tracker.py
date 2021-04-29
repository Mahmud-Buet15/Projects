from bs4 import BeautifulSoup
import requests
import smtplib


#the mail id which will be used to send message
my_email="redwan.ahmed1512039@gmail.com"
password="Redwan(1)"

#the product page which i'm interested in
url="https://www.amazon.com/AMD-Ryzen-3700X-16-Thread-Processor/dp/B07SXMZLPK/ref=sr_1_6?dchild=1&qid=1619678844&rnid=541966&s=electronics&sr=1-6"
header={"Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}
response=requests.get(url,headers=header)

response.raise_for_status()  #checking for errors

website=response.text

soup=BeautifulSoup(website,"html.parser")  #making soup object

title=soup.title.text
# print(title)

price=soup.find(name="span",class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()

#removing the currency symbol
final_price=float(price[1:])

# print(final_price)


#if the price is less than 280 i'll get a message
if final_price<280:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rootovermahmud@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{title}\n is now at {final_price}\n{url}"
            )
    