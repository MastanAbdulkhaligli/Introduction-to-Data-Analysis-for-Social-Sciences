# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:27:01 2021

@author: User
"""

my_list = []
for item in range(6):
    usr_input = int(input("Enter value:"))
    if(usr_input <0):
        break
    else:
        my_list.append(usr_input)
        
print("Average is : ", sum(my_list)/len(my_list))


    