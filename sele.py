from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

import time

from data.py import *

#open selenium browser 
options = webdriver.ChromeOptions()
options.add_argument("--headless=new") #leave this commented so browser appears
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

#gets all the b's (ie titles anad etc) in the page
page_b = driver.find_elements(By.TAG_NAME, 'b')

# print item names as single list
for item in page_b[15:]:
    if item.text == "Search Neopets:":
        break
    print(item.text)




#prevents selenium browser from autoclosing (when commented out)
# time.sleep(20) 