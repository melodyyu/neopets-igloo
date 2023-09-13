
#filter inventory file. if name is in file already, don't include here
with open("inventory.txt") as file:
  item_names = []
  item_prices = [] 
  for line in file:
    index = line.index(":")

    #items until : are names, after are costs
    item_names.append(line[:index])
    item_prices.append(line[index+1:].strip())

file.close()

print("ITEM SIZE: ", len(item_names), "\n \n", item_names)
print("PRICE SIZE: ", len(item_prices), "\n \n", item_prices)
