# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:03:26 2021

@author: Mastan Abdulkhaligli
21403007
"""

# Get input from user
barcode = input("Enter a GTIN-8 barcode:")

if((barcode[0:3]=='868') or (barcode[0:3]=='869')):
    print('This is an item of a company registered in Turkey.')

else:
    print("This is an item of a company registered elsewhere. ")
    

first_7 = barcode[0:len(barcode)-1]
check_sum_first = int(barcode[-1])

# Sum all digits in odd positions
odd = first_7[0:len(barcode):2]

odd_sum = int(odd[0]) + int(odd[1])  + int(odd[2]) + int(odd[3])


# Sum all digits in even positions and multiply by 3
even = first_7[1:len(barcode)-1:2]

even_sum = (int(even[0]) + int(even[1])  + int(even[2]) ) *3


# Add both results together  and take the modulus/remainder of this number by 10 
total_sum = odd_sum + even_sum
remainder  =  total_sum % 10 


if remainder ==0:
    check_sum = 0

else:
    check_sum = 10 - remainder


# Final Part 
if check_sum == check_sum_first:
    print("Check digit is correct")

else:
    print("Check digit is faulty.","It should be: ",check_sum)
    








