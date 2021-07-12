# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:16:43 2021

@author: User
"""
my_list = []
for names in range(15):
    usr_input = input("Enter name:")
    
    
    if ((usr_input.lower() != "stop") or usr_input.lower != "quit"):
        usr_title = input ("Enter title:")
        last_index = usr_input.rfind(' ')
        first_name = usr_input[0:last_index]
        last_name = usr_input[last_index +1 :]

        print("Official name:", first_name, ",", usr_title, last_name)
        
    
    else:
        break
    print("Program complete.... ")
        
    

    