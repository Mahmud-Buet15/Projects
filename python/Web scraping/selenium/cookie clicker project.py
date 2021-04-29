from selenium import webdriver
import time

chrome_driver_path="C:\Development\chromedriver.exe"

driver=webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie=driver.find_element_by_id("cookie")
five_min = time.time() + 60*5     # 5minutes
increment=10
while True:
    timeout=time.time()+increment  #10 seconds from now
    increment+=1

    while True:
        test=0
        cookie.click()
        if test==increment or time.time()>timeout:
            break
        test-=1
        
    
    money=driver.find_element_by_id("money")
    money=int(money.text.replace(",",""))
    
    #objects
    cursor=driver.find_element_by_id("buyCursor")
    grandma=driver.find_element_by_id("buyGrandma")
    factory=driver.find_element_by_id("buyFactory")
    mine=driver.find_element_by_id("buyMine")
    shipment=driver.find_element_by_id("buyShipment")
    alchemy_lab=driver.find_element_by_id("buyAlchemy lab")
    portal=driver.find_element_by_id("buyPortal")
    time_machine=driver.find_element_by_id("buyTime machine")
    
    #money to buy objects
    cursor_money=int(cursor.text.split("\n")[0].split("-")[1].replace(",",""))
    grandma_money=int(grandma.text.split("\n")[0].split("-")[1].replace(",",""))
    factory_money=int(factory.text.split("\n")[0].split("-")[1].replace(",",""))
    mine_money=int(mine.text.split("\n")[0].split("-")[1].replace(",",""))
    shipment_money=int(shipment.text.split("\n")[0].split("-")[1].replace(",",""))
    alchemy_lab_money=int(alchemy_lab.text.split("\n")[0].split("-")[1].replace(",",""))
    portal_money=int(portal.text.split("\n")[0].split("-")[1].replace(",",""))
    time_machine_money=int(time_machine.text.split("\n")[0].split("-")[1].replace(",",""))

    
    
    
    
    if money>time_machine_money:
        time_machine.click()
    elif money>portal_money:
        portal.click()
    elif money>alchemy_lab_money:
        alchemy_lab.click()
    elif money>shipment_money:
        shipment.click()
    elif money>mine_money:
        mine.click()
    elif money>factory_money:
        factory.click()
    elif money>grandma_money:
        grandma.click()
    elif money>cursor_money:
        cursor.click()
    
    time.sleep(1)

    
    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
    
driver.quit()
    




