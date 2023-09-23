from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

import time
import re 

from collections import OrderedDict
    
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

counter = 0
total_time = 0
for i in range(10):
    start = time.time()

    #get item information
    form_items = driver.find_element(By.NAME, "items_for_sale")
    item_details = form_items.text.split('\n')
    # print(item_details)

    #get all item names and costs. 
    inventory = []
    costs = []
    for item in item_details:
        if len(item) > 2 and bool(re.search(r'\d', item)) == False:
            inventory.append(item) #Returns single list of strings
        if "Cost : " in item:
            cost = re.findall(r'[\d]+', item) #Returns list of lists 
            costs.append(cost)
    # print(inventory, "\n", costs)

    #flattens prices into single list
    item_costs = []
    for list in costs:
        for item in list: 
            item_costs.append(item)
    # print(item_costs)


    #sanity check -- if inventory and price arrays differ in size, stop here
    if len(inventory) == len(item_costs):
        print("NAME/PRICE ARRAYS ARE GOOD TO GO, GREAT SIZE:", len(inventory))

        inv_dict = dict(zip(inventory, item_costs))

        with open("inventory.txt", "a+") as file:
            file.seek(0) #starts looking through top of file
            file_line = file.read().splitlines()
            # print("this is the file line (size: ", len(file_line), "): \n", file_line)

            #if file is empty, append entire inventory list to it
            if len(file_line) == 0:
                print("Nothing in file so far")
                for key, value in inv_dict.items():
                    file.write(key+":"+value+"\n")

            # #if file is not empty, check name against existing entries; add only if no dupes           
            else: 
                print("File occupied")        

                content_list = set() #store existing names in txt file for ez lookup
                new_items = [] #items that aren't currently in txt file

                #take names currently in file and add to set 
                for line in file_line:
                    index = line.index(":")
                    content_list.add(line[:index])

                #check if the items in inv_dict is new; add if it is 
                for item in range(len(inventory)):
                    if inventory[item] not in content_list:
                        new_items.append(inventory[item])
                        content_list.add(inventory[item]) 

                # print(new_items)
                # print(content_list)
                
                #append new items to txt file as name:price 
                for new_item in new_items:
                    file.write(new_item+":"+inv_dict[new_item]+"\n")

        file.close()

        #file and inventory stats
        print("FILE IS THIS LONG:{}, PAGE INVENTORY IS THIS LONG:{}".format(len(file_line), len(inv_dict)))
        print(inv_dict, '\n\n\n\n', file_line)  

    else:
        print("OUR SHIP IS TAKING ON WATER", len(inventory), len(item_costs))


    #If commented out, prevents selenium browser from autoclosing after script runs
    time.sleep(45) #use this to run the script multiple times --this is the time block in between

    #stats on how many times it's been run and how long it takes
    counter += 1 
    end = time.time()
    interval_time = end-start-20
    total_time = total_time + (end-start)
    print("ROUND:{}".format(counter), '\n', 'TIME NEEDED FOR THIS ROUND TO RUN: {:.2f}'.format(interval_time),
                             '\n','TOTAL TIME TAKEN: {:.2f}'.format(total_time), '\n\n\n\n\n\n') 


#run script multiple times 
# def main():
#     for i in range(5):

#         time.sleep(60)
        #run all the actions in this script