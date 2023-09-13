import pandas as pd

#import other files in directory
import filter


# df = pd.DataFrame(columns=['Name', 'Igloo Price', 'Jellyneo Price', 'Category'])

##Create dF with dictionary of lists 
data = {
    "Name": filter.item_names,
    "Igloo Prices": filter.item_prices
}

df = pd.DataFrame(data)
print(df)