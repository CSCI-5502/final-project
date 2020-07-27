import pandas as pd 
import numpy as np 

dictionary = {'test': [0,None,0,0,0]}
df = pd.DataFrame.from_dict(dictionary)
col = df['test']
print(col)
result = col.isna().sum()
print(result)