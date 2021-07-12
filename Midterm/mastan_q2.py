# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:06:31 2021

@author: Mastan Abdulkhaligli
"""


# We create array and fill it with 1 -5 but list start with 0.  
import random

my_list = []

for item in range(5):
    inp = input("Enter a word:")
    my_list.append(inp)
    

random_int = (random.randint(1,5))

# I extract -1 because it can give out of bound error and 0 index will never shown
print("Displaying word #",random_int,":",my_list[random_int-1])

