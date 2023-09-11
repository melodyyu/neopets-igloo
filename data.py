import pandas as pd
import sele


#Create dF with column names
# df = pd.DataFrame(columns=['Name', 'Igloo Price', 'Jellyneo Price', 'Category'])
df = pd.DataFrame(sele.data)

print(df)