"""Mastan Abdulkhaligli
21403007 CS
Lab 03"""

# Part 3


import math

# Enter integer number
inp1 = int(input("Enter an integer number: "))

# Update input variable to abs value of itself
inp1=abs(inp1)
print("The absolute value of the number is: ",inp1)

# Finding square root of input
sqr_inp1 = math.sqrt(inp1)
# Round to lowest limit using floor function
lower_limit = math.floor(sqr_inp1)

# Round to highest limit using ceil function
upper_limit = math.ceil(sqr_inp1)

print(sqr_inp1,"is in between",lower_limit, "and", upper_limit)

