# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:12:56 2021

@author: User
"""
# Part a

my_data = {"Albert Einstein": "03/14/1879",
           "Sky Brown": "07/12/2008",
           "Ada Lovelace": "12/10/1815",
           "Rudy Huxtable": "06/14/2016",
           "Rowan Atkinson": "01/06/1955",
           "Stephen Hawking": "01/08/1942"}



# Part b 
temp = ""

for item in my_data:
    temp = my_data[item]
    re_use = my_data[item]
    temp = temp[6:len(temp)]
    temp = int(temp)
    
    if( (2021-temp) >= 18):
        my_data[item] = (re_use,"adult")
        
    else:
        my_data[item] = (re_use,"child")
        



# Part C

user = input("Whose birthday do you want to look up?\n")
if user in my_data:
    print(user + "'s", "birthday is", my_data[user][0])
else:
    print("Sadly, we don't have",user,"'s", "birthday")
