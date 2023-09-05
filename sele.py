from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

import time


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
print("clicked it")

#gets all the b's (ie titles anad etc) in the page; prints only the content ones
page_b = driver.find_elements(By.TAG_NAME, 'b')

# print(type(page_b)) #is a list
for item in page_b[13:]:
    if item.text == "Search Neopets:":
        break
    print(item.text)
    

#see what the pagesource returns --> stored in igloo_innerhtml
# page_source = driver.execute_script("return document.body.outerHTML;")
# print(page_source)

#works -> stored in igloo_grabdivcontent
# content = driver.find_element(By.ID, "content").get_attribute("innerHTML")
# print (content)

#stored in igloo_form_itemstext
# form_items = driver.find_element(By.NAME, "items_for_sale")
# print(form_items) #returned name of all items being sold, as well as their inventory and cost
#^ without .text, returned blank
# for item in form_items:
    # print(item.text)


#this returns the same output as igloo_form_itemstext
# inventory = driver.find_elements(By.XPATH, '//*[@name="items_for_sale"]/table/tbody')
# print(inventory)

# soup = BeautifulSoup(html, 'lxml')
# element = driver.find_element(By.)
# element.get_attribute('innerHTML')

# print("soup", soup, "\n") #returns blank



# time.sleep(20) #prevents selenium browser from autoclosing. if i want to speed up the script, comment this out so to not wait on browser to close. 
