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

#deal with exceptions
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import time
import re

import clean
    
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

item_names = clean.filter_names()



def timer(start,end):
  hours, rem = divmod(end-start, 3600)
  minutes, seconds = divmod(rem, 60)
  formatted_time = f"{int(hours):02}:{int(minutes):02}:{seconds:05.2f}"
  return formatted_time
  # print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
  

round = 0
script_start = time.time()

jn_prices = []
categories = [] 
for name in item_names:
  iter_timer = time.time()
  print("ROUND: {}".format(round))

  #wait for element to be clickable 
  try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "search-name")))
    print("WAITED FOR ELEMENT TO BE CLICKABLE")
  except TimeoutException as e:
    print("TimeoutException occurred because it took too long to click: {}".format(iter_timer))

  #put input into jn search bar - need to be in forloop to refind element
  search_bar = driver.find_element(By.ID, "search-name")

  try:
    search_bar.click()
  except StaleElementReferenceException as e:
    print("StaleElementReferenceException occurred:", str(e))

  search_bar.clear()
  print("CLEARING SEARCH BAR")
  search_bar.send_keys(name)
  print("INPUT THIS: {}".format(name))
  search_bar.submit()
  print("SUBMITTED")

  #wait for new page to load then grab elements 
  try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/ul[2]/li/span")))
    print("WAITING FOR NEW PAGE TO LOAD")
  except TimeoutException as e:
    exception_timer = time.time()
    print("TimeoutException occurred because it took this long to load: {}".format(timer(iter_timer, exception_timer)))
  
  #handle specific cases; otherwise, deal with exceptions normally
  if "Wall Paint" in name or "Floor Tiles" in name:
    print("IT WAS EITHER A WALL PAINT OR A FLOOR TILE -- ", name)
    jn_price = 0
  else:
    #extract price - if none, print 0 and continue
    try:
      jn_text = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/ul[2]/li/span").text
      print("FOUND ELEMENT")

      #remove extra, return only digits
      jn_price = re.sub("\D","",jn_text) 
    except NoSuchElementException as e:
      print("Element didn't have a price; added as 0 instead")
      jn_price = 0

  print("PRICE: {}".format(jn_price))
  jn_prices.append(jn_price)
  print('\n', jn_prices, '\n')
  
  link_locator = "//a[text()='" + name + "']"
  #click the item's link
  try:
    link_element = driver.find_element(By.XPATH, link_locator)
    link_element.click()
  except NoSuchElementException as e:
    print("NoSuchElementException")

  #find the category
  
  try:
    partial_text =  '- This is the official type for this item on Neopets.'
    category_locator = "//li[contains(text(), '" + partial_text + "')]/a/strong" #find category based off description string
    category = driver.find_element(By.XPATH, category_locator).text
    print(category)
  except NoSuchElementException as e:
    print("NoSuchElementException, so put None instead")
    category = "None"
    
  categories.append(category)
  print("CATEGORY: {}".format(category))
  print('\n', categories, '\n')

  round+=1 

#print total time it's taken to run:
script_end = time.time()
print("TOTAL TIME TAKEN TO RUN JN SCRIPT: {}".format(timer(script_start, script_end)))
# driver.quit()


# add prices to inventory.txt; separate with -
with open("inventory.txt", "r+") as file:
  file.seek(0) #sets cursor at top of file; "a+" auto puts it at end
  file_line = file.read().splitlines()

  #add to file only if length of file and price array match
  if len(file_line) == len(jn_prices) == len(categories):
    print("SIZES ARE A MATCH -- GOING IN")
    #read line by line; after each line, add jn price and categories
    modified_lines = []
    for line in range(len(file_line)):
      modified_line = file_line[line] + "-" + str(jn_prices[line]) + ";" + categories[line] + '\n'
      modified_lines.append(modified_line)
    file.seek(0) #reset cursor 
    file.writelines(modified_lines)
      # file.write(file_line[line]+";")
  else:
     print("{} != {} != {}. FILE SIZE AND ARRAY LENGTH DIDN'T MATCH -- ABORT!".format(len(file_line), len(jn_prices), len(categories)))
file.close()

