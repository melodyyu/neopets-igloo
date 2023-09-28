#take inventory.txt file and isolate info into two lists: names and prices. 
def filter_inventory():

  with open("inventory.txt") as file:
    item_names = []
    item_prices = [] 
    jn_prices = [] 

    for line in file:
      index = line.index(":")
      index_semi = line.index(";")

      #items until : are names, after are costs
      item_names.append(line[:index])
      item_prices.append(line[index+1:index_semi])
      jn_prices.append(line[index_semi+1:].strip())

  file.close()
  return item_names, item_prices, jn_prices


#see all lists and corresponding lengths
def print_lists(item_names, item_prices, jn_prices):
  if len(item_names) == len(item_prices) == len(jn_prices):
    print("SIZES ARE GOOD -- WE'RE ALL {}".format(len(item_names)))
  else:
    print("OH NO -- ITEM NAMES: {}, PRICE SIZE: {}, JN_PRICE SIZE: {}". format(len(item_names), len(item_prices), len(jn_prices)))

  print("ITEMS: \n{}\n".format(item_names))
  print("PRICE: \n{}\n".format(item_prices))
  print("JN_PRICE: \n{}\n".format(jn_prices))


#only executes when this script is run directly; not when it's imported into another file
if __name__ == "__main__":
  item_names, item_prices, jn_prices = filter_inventory()
  print_lists(item_names, item_prices, jn_prices)