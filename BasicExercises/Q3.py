# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:40:45 2021

@author: User
"""
import random
my_list = []
for f in range(10):my_list.append(random.randint(1,21))
print("The list is:", my_list)

num_occurence = []
numbers = []
for item in my_list:
    if item not in numbers:
        numbers.append(item)
        num_occurence.append(my_list.count(item))

for count in range(len(numbers)):
    print("The number", numbers[count] , "appears", num_occurence[count], "times.")
        
        
        

