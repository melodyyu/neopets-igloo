from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

import time

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


#