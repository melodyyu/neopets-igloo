
#filter inventory file. if name is in file already, don't include here
with open("inventory.txt") as file:
  inventory = []
  for line in file:
    inventory.append(line.strip()) 
file.close()

print("SIZE: ", len(inventory), "\n \n", inventory)
