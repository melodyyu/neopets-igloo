""" This script takes the information from inventory.txt (which at this point
is populated with names, igloo prices, jellyneo prices and jellyneo categories)
and isolate the information into individual lists"""

#take inventory.txt file and isolate just the names
def filter_names():
  item_names = [] 
  with open("inventory.txt") as file:
    item_names = []

    for line in file:
      index = line.index(":")

      #items until : are names, after are costs
      item_names.append(line[:index])
  file.close()
  return item_names

#isolate other info from inventory.txt into respective lists
def filter_inventory():

  with open("inventory.txt") as file:
    item_prices = [] 
    jn_prices = [] 
    categories = [] 

    for line in file:
      index = line.index(":")
      index_dash = line.index("-")
      index_semi = line.index(";")

      #items until : are names, after are costs
      item_prices.append(line[index+1:index_dash])
      jn_prices.append(line[index_dash+1:index_semi])
      categories.append(line[index_semi+1:].strip())
      

  file.close()
  return item_prices, jn_prices, categories


#see all lists and corresponding lengths
def print_lists(item_names, item_prices, jn_prices, categories):
  if len(item_names) == len(item_prices) == len(jn_prices) == len(categories):
    print("SIZES ARE GOOD -- WE'RE ALL {}".format(len(item_names)))
  else:
    print("OH NO -- ITEM NAMES: {}, PRICE SIZE: {}, JN_PRICE SIZE: {}, CATEGORIES: {}".format(len(item_names), len(item_prices), len(jn_prices), len(categories)))

  print("ITEMS: \n{}\n".format(item_names))
  print("PRICE: \n{}\n".format(item_prices))
  print("JN_PRICE: \n{}\n".format(jn_prices))
  print("CATEGORIES: \n{}\n".format(categories))



#only executes when this script is run directly; not when it's imported into another file
if __name__ == "__main__":
  item_names = filter_names()
  item_prices, jn_prices, categories = filter_inventory()
  print_lists(item_names, item_prices, jn_prices, categories)