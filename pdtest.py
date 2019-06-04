import pandas as pd # This is the standard

# Reading a csv into pandas
df =  pd.read_csv('D:/develop/python/python_workspace/uk_rain_2014.csv',header=0)

# Gettinng first x rows.
df.head(5)

print(df.head(5))