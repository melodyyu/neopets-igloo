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



#get all item names and return as single list of strings
page_b = driver.find_elements(By.TAG_NAME, 'b')
inventory = []
for count, item in enumerate(page_b[13:]):
    if item.text == "Search Neopets:":
        break
    # print(count, item.text)
    inventory.append(item.text)
print(inventory)

#get item prices
form_items = driver.find_element(By.NAME, "items_for_sale")

item_details = form_items.text.split('\n')
# print(item_details)

item_prices = []
for item in item_details:
    if "Cost : " in item:
        cost = re.findall(r'[\d]+', item) #works but returns list of lists 
        item_prices.append(cost)
# print(item_prices)

#flattens prices into single list
flat_prices = []
for list in item_prices:
    for item in list: 
        flat_prices.append(item)
print(flat_prices)


#sanity check -- if inventory and price arrays differ in size, stop here
if len(inventory) == len(flat_prices):
    print("GREAT SIZE: ", len(inventory))

    #output item names to .txt file
    with open("inventory.txt", "a") as file:
        for name in inventory:
            file.write(name+"\n")
    file.close()
else:
    print("OUR SHIP IS TAKING ON WATER", len(inventory), len(flat_prices))


#If commented out, prevents selenium browser from autoclosing after script runs
# time.sleep(20) 