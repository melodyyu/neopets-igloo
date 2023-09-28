import pandas as pd

#import other files in directory
import clean


# df = pd.DataFrame(columns=['Name', 'Igloo Price', 'Jellyneo Price', 'Category'])
item_names, item_prices, jn_prices = clean.filter_inventory()

##Create dF with dictionary of lists 
data = {
    "Name": item_names,
    "Igloo Prices": item_prices, 
    "JN Prices": jn_prices
}

df = pd.DataFrame(data)
print(df)