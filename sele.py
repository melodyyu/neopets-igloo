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
for i in range(2):
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
        print("GREAT SIZE: ", len(inventory))

        #outputs item name,cost to .txt file
        # with open("inventory.txt", "a+") as file:
        #     #set file pointer to top of file (it defaults at end)

    
 
        inv_dict = OrderedDict(zip(inventory, item_costs)) #create dictionary from the two lists
        #     #write inventory as name:price pairs
        #     for key,value in inv_dict.items():
        #         file.seek(0)
        #         file_line = file.read().splitlines()
        #         print(file_line)

        #         if key not in file_line:
        #             file.write(key+":"+value+"\n")
        #         else:
        #             pass
        # file.close()
        # print(inv_dict)


        # for key,value in inv_dict.items():
        #     with open("inventory.txt", "a+") as file:

        #         file.seek(0)
        #         file_line = file.read().splitlines()
        #         # print(file_line)

        #         print(len(file_line))
                
        #         # for line in file_line: 
                        
        #         #     if key not in file_line:
        #         #         print(key, value)
        #         #         file.write(key+":"+value+"\n")

        #             # print("already in")
        #         #     pass
        #         # else: 
        #         #     file.write(key+":"+value+"\n")
        #     file.close()
        # print(inv_dict)

        with open("inventory.txt", "a+") as file:
            file.seek(0)
            file_line = file.read().splitlines()
            # print("this is the file line (size: ", len(file_line), "): \n", file_line)

            # for i in file_line:
            #     print(i)
            #if file is empty, append entire inventory list to it
            if len(file_line) == 0:
                print("Nothing in file so far")
                for key, value in inv_dict.items():
                    file.write(key+":"+value+"\n")


            # else:
            #     file_line = dict(file_line)
            #     for key, value in inv_dict:
            #         if key not in file_line: 
            #             file.write(key+":"+value+"\n")
            #             print("wrote something, SPECIFICALLY: {}:{}".format(key, value))


            # #if file is not empty, check name against existing entries; add only if no dupes           
            # else: 
                print("im in here")
                for key,value in inv_dict.items():
                    for i in range(len(file_line)):
 
                        print("compared {} and {}, round:{}".format(key, file_line[i],i))
                        if key not in file_line[i]:
                            print("wrote something, SPECIFICALLY: {}:{}".format(key, value))
                            file.write(key+":"+value+"\n")
                            # i+=1
                            # break #--->gets stuck on round1 max. without it, checks for dupe, but then proceeds to add it like len(file_line-1) times to inventory file
                        else:
                            print("BROKE OUT BC OF {} and {}".format(key, file_line[i]))
                            # i+=1
                            # break
                        i+=1
                        # break #--> doesnt increment rounds at all
                    # break
                        
                # result = any(key in file_line for key, value in inv_dict.items())
                # print(result)
                # if result == False: #key does not exist in txt file
                #     file.write(key+":"+value+"\n")       
                #     print("wrote something, specifically:", key+":"+value)

                # for line in file_line:
                #     for key, value in inv_dict.items():      
                #         print(type(key), type(file_line))       
                #         result = any(key in file_line for key in inv_dict.items())       
                #         if result == False:
                #             print("NOT IN:", key, value)
                #             file.write(key+":"+value+"\n")
        file.close()
        print("FILE IS THIS LONG:{}, PAGE INVENTORY IS THIS LONG:{}".format(len(file_line), len(inv_dict)))
        print(inv_dict)

    else:
        print("OUR SHIP IS TAKING ON WATER", len(inventory), len(item_costs))


    #If commented out, prevents selenium browser from autoclosing after script runs
    time.sleep(20) #use this to run the script multiple times --this is the time block in between
    counter += 1 
    end = time.time()
    interval_time = end-start-20
    total_time = total_time + (end-start)
    print("ROUND: ", counter, '\n', 'TIME NEEDED TO RUN: ', "{:.2f}".format(interval_time), '\n',
                         'TOTAL TIME TAKEN: ', "{:.2f}".format(total_time), '\n\n\n\n\n') 


#run script multiple times 
# def main():
#     for i in range(5):

#         time.sleep(60)
        #run all the actions in this script