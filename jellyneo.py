from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

#for explicitly waiting
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import time
import re

import filter
    
#open selenium browser 
options = webdriver.ChromeOptions()
options.add_argument("--headless=new") #leave this commented for browser to appear
options.page_load_strategy = 'none'

chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)

driver = Chrome(options = options, service=chrome_service)
driver.implicitly_wait(5) #need this so site can load before next step


#input site
url = 'https://items.jellyneo.net/'
driver.get(url)


#put input into jn search bar 
search_bar = driver.find_element(By.ID, "search-name")

#take input from df name row
name = "Simple Yellow Chair"
# for name in filter.item_names:
search_bar.send_keys(name)
search_bar.submit()
#wait for new page to load then grab elements 
element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/ul[2]/li/span")))

#extract price
jn_prices = []
jn_text = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/ul[2]/li/span").text

jn_price = re.sub("\D","",jn_text) #remove extra, return only digits
print(jn_price)

jn_prices.append(jn_price)
print(jn_prices)


driver.quit()

  
#look at the resulting page. save the price & category in respective array (or dictionary)
  #what if i just add it to inventory.txt by separating it with ; or - 
  #or would it be better if i return arrays in this file 