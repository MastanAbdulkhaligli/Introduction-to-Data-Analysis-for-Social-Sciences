# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:03:00 2021

@author: Mastan Abdulkhaligli
"""

import numpy as np
import pandas as pd

# Part a 
data2000 = pd.read_excel("education_gdp_2000_10.xlsx")
data2005 = pd.read_excel("education_gdp_2015.xlsx")

# Part B
My_inner = pd.merge(left = data2000,right = data2005,left_on="Country",right_on= "Country")

# Part C
My_inner = My_inner.replace(to_replace = '..',value = np.nan)

# Part D
My_inner =  My_inner.dropna()
print(My_inner)

# Part E

My_inner['mean'] =  My_inner.iloc[:,1:3].mean(axis=1)
print(My_inner)

# Part F
My_inner.to_excel("avg_countries.xlsx",index= None)

