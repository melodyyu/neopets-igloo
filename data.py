import pandas as pd

#import other files in directory
import clean


# df = pd.DataFrame(columns=['Name', 'Igloo Price', 'Jellyneo Price', 'Category'])
item_names = clean.filter_names()
item_prices, jn_prices, categories = clean.filter_inventory()

##Create dF with dictionary of lists 
data = {
    "Name": item_names,
    "Igloo Price": item_prices, 
    "JN Price": jn_prices,
    "Categories": categories
}

df = pd.DataFrame(data)
print(df)