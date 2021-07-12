# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:44:18 2021

@author: Mastan
Lab07
"""

import numpy as np 

x= np.array([2,3,5,7,13])
x = pow(2,x-1) * (pow(2,x)-1)
print("Result:",x)
