import pandas as pd
import numpy as np
print ("Started")

df1 = pd.read_csv('train.csv', encoding = 'latin-1')
print('Loaded dataset')
#print(df1.head())
print('Starting Filtering')

#df2 = pd.DataFrame()

#df3 = pd.DataFrame()

#print(df2.head())


df2 = df1.drop(df1[df1.click == 0].index)

df3 = df1.drop(df1[df1.click == 1].index)

print("Filtering Done")
#print (df2.head())

df2.to_csv('ones.csv', encoding='utf-8', index=False)

df3.to_csv('zeros.csv', encoding='utf-8', index=False)

print("File Saved")