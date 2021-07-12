"""Mastan Abdulkhaligli 
21403007
Lab 02 """
#First Part 

# Enter Number 
myNum = input("Enter a number: ")
lab2 = 25

# Print Number 
print("myNum is ", type(myNum), " and its value is ", myNum)
print("lab2 is ", type(lab2), "and its value is ", lab2)

# Subtract 250 from lab2 and display.
lab2=lab2-250
print(lab2)

#Subtract 250 from myNum and display -> What happens??
"""myNum=myNum-250
print(myNum)"""

""" When we take input we take as a string if we want to take input as a int then we should :  """ # myNum = int(input("Enter a number: "))

# Convert myNum to an int value. 
myNum = int(myNum)
# Subtract 100 from myNum and display. 
myNum= myNum-100
print(myNum)

#  Create string: ‘This course is CS125’
str1= "This course is CS125"

# Print the first and last characters.

# First
print("First character: ",str1[0])

# Last
print("Last character: ",str1[-1])

# Print the second and last words in the string. 
print("Second word: ", str1.split()[1])

# Last Word
print("Last word: ", str1.split()[-1])


