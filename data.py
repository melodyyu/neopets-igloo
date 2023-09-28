import pandas as pd

#import other files in directory
import clean


# df = pd.DataFrame(columns=['Name', 'Igloo Price', 'Jellyneo Price', 'Category'])

##Create dF with dictionary of lists 
data = {
    "Name": clean.item_names,
    "Igloo Prices": clean.item_prices, 
    "Jellyneo Prices": clean.jn_prices
}

df = pd.DataFrame(data)
print(df)