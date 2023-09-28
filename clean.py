#take inventory.txt file and isolate info into two lists: names and prices. 
def filter_inventory():

  with open("inventory.txt") as file:
    item_names = []
    item_prices = [] 

    for line in file:
      index = line.index(":")

      #items until : are names, after are costs
      item_names.append(line[:index])
      item_prices.append(line[index+1:].strip())

  file.close()
  return item_names, item_prices


#see all lists and corresponding lengths
def print_lists(item_names, item_prices):
  print("ITEM SIZE: {}\n{}".format(len(item_names), item_names))
  print("PRICE SIZE: {}\n{}".format(len(item_prices), item_prices))

#only executes when this script is run directly; not when it's imported into another file
if __name__ == "__main__":
  item_names, item_prices = filter_inventory()
  print_lists(item_names, item_prices)