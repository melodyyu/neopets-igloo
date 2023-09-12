from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

import time
import re 

# from data.py import *

#open selenium browser 
options = webdriver.ChromeOptions()
options.add_argument("--headless=new") #leave this commented for browser to appear
options.page_load_strategy = 'none'

chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)

driver = Chrome(options = options, service=chrome_service)
driver.implicitly_wait(5) #need this so site can load before next step


#input site
url = 'https://www.neopets.com/winter/igloo.phtml'
driver.get(url)


#gather login elements. input credentials and enter site
username = driver.find_element(By.ID, "loginUsername")
password = driver.find_element(By.ID, "loginPassword")
login = driver.find_element(By.ID, "loginButton")

username.send_keys("heartspade1")
password.send_keys("nono70smoothie")

login.click() 
print("Logged in whee")

driver.implicitly_wait(15)

#enter igloo
igloo_entrance = driver.find_element(By.LINK_TEXT, "here").click()
print("Entered igloo")


#get item information
form_items = driver.find_element(By.NAME, "items_for_sale")
item_details = form_items.text.split('\n')
# print(item_details)

#get all item names and costs. Return as single list of strings
inventory = []
costs = []
for item in item_details:
    if len(item) > 2 and bool(re.search(r'\d', item)) == False:
        inventory.append(item)
    if "Cost : " in item:
        cost = re.findall(r'[\d]+', item) #works but returns list of lists 
        costs.append(cost)
print(inventory, "\n", costs)

#flattens prices into single list
item_costs = []
for list in costs:
    for item in list: 
        item_costs.append(item)
print(item_costs)


#sanity check -- if inventory and price arrays differ in size, stop here
if len(inventory) == len(item_costs):
    print("GREAT SIZE: ", len(inventory))

    #outputs item name,cost to .txt file
    with open("dict.txt", "a") as file:
        inv_dict = dict(zip(inventory, item_costs))
        for key,value in inv_dict.items():
            file.write(key+" "+value+"\n")
    file.close()
    print(inv_dict)

else:
    print("OUR SHIP IS TAKING ON WATER", len(inventory), len(item_costs))


#If commented out, prevents selenium browser from autoclosing after script runs
# time.sleep(20) 