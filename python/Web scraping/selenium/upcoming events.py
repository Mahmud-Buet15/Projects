from selenium import webdriver
import pandas as pd

chrome_driver_path="C:\Development\chromedriver.exe"

driver=webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.python.org/")

#for single date
# event_time=driver.find_element_by_css_selector(".event-widget.last div.shrubbery .menu li time")
# print(event_time.get_attribute("datetime").split("T")[0])

event_times=driver.find_elements_by_css_selector(".event-widget.last div.shrubbery .menu li time")
times=[time.get_attribute("datetime").split("T")[0] for time in event_times]


event_names=driver.find_elements_by_css_selector(".event-widget.last div.shrubbery .menu li a")
events=[event.text for event in event_names]


#making a dictionary of event times and names
event_dict=dict()
for i in range(len(event_names)):
    event_dict[i]={
        "time":times[i],
        "name":events[i]
        }
    
print(event_dict)

#another option
# df=pd.DataFrame(list(zip(times,events)),columns=["time","name"])
# event_dict=df.to_dict("index")
# print(event_dict)

driver.quit()