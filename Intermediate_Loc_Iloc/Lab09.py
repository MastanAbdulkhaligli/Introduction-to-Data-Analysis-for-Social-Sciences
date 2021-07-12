# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:31:51 2021

@author: Mastan Abdulkhaligli
21403007
CS
Lab09
"""

import matplotlib as plt
import numpy as np 
import pandas as pd

# a)
df = pd.read_excel("glastonbury.xlsx")
print(df)

# b)
df.set_index(['ticknumb'],inplace= True)
print(df)

# c)
print(df['music'].unique())

# d)
print(df.iloc[[2,3,4],[0,3]])

# e)
df = df.dropna()
print(df)

# f)
print(df[['music','change']])

# g)
print(df.loc[df['music'] == 'Metaller'])

# h)
print(df[df.day3 == df.day3.max()])

#i)
print(df[df.change > 0])

# j)
temp2 =  df[df.change == df.change.min()]
print(temp2.music)



# k)
temp = df[df.day1 > 2.5]
temp = temp[(temp['music']=='Crusty') | (temp['music']=='Indie Kid') ]
print(temp)

# l)
print(df.loc[[4196,4398],['music','change']])









