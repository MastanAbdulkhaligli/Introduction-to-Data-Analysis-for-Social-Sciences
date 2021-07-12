# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 13:35:19 2021

@author: Mastan Abdulkhaligli
Lab 08
"""

import numpy as np 
import pandas as pd

# Part A
tour1 = ['Melbourne', 'Istanbul', 'New York', 'Barcelona', 'London', 'Rome', 'Berlin', 'Toronto'] 
tour2 = ['Istanbul', 'London', 'Barcelona', 'Rome', 'Stockholm', 'Berlin', 'Madrid']


male = [1000, 2500, 950,820, 706, 540, 1030, 650] 
female = [450, 720, 410, 200, 250, 605, 560]

# Part B
data1 = pd.Series(male,index = tour1)
data2 = pd.Series(female,index = tour2)

# Part C
data = data1 + data2
print(data)

# Part D
dataNew = data.fillna(0)

# Part E
print(dataNew.head(4))

# Part F
print(dataNew["Istanbul": "Rome"])

# Part G
print(dataNew[dataNew>0])


# Part H
Europe = dataNew.drop(labels=["Melbourne","New York","Toronto"])
print(Europe)
