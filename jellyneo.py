from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

#for explicitly waiting
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#for new inputs
from selenium.webdriver.common.keys import Keys

#deal with stale elements
from selenium.common.exceptions import StaleElementReferenceException

import time
import re

import filter
    
#open selenium browser 
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new") #leave this commented for browser to appear
options.page_load_strategy = 'none'

chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)

driver = Chrome(options = options, service=chrome_service)
driver.implicitly_wait(5) #need this so site can load before next step


#input site
url = 'https://items.jellyneo.net/'
driver.get(url)




round = 0
jn_prices = []
for name in filter.item_names:
  print(round)

  #wait for element to be clickable 
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "search-name")))
  print("I WAITED")

  #put input into jn search bar - need to be in forloop to refind element
  search_bar = driver.find_element(By.ID, "search-name")

  try:
    search_bar.click()
  except StaleElementReferenceException as e:
    print("StaleElementReferenceException occurred:", str(e))

  search_bar.clear()
  print("CLEARING")
  search_bar.send_keys(name)
  print("INPUT THIS: {}".format(name))
  search_bar.submit()
  print("SUBMITTED")

  #wait for new page to load then grab elements 
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/ul[2]/li/span")))
  print("WAITING")

  #extract price
  jn_text = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/ul[2]/li/span").text
  print("FOUND ELEMENT")

  #remove extra, return only digits
  jn_price = re.sub("\D","",jn_text) 
  print(jn_price)

  jn_prices.append(jn_price)
  print('\n', jn_prices, '\n')
  round+=1 
  # time.sleep(5)

# driver.quit()

  
#look at the resulting page. save the price & category in respective array (or dictionary)
  #what if i just add it to inventory.txt by separating it with ; or - 
  #or would it be better if i return arrays in this file 