"""Mastan Abdulkhaligli
CS 21403007
Lab 04  """
import math

# Part 3 

# Number of adults between ages 16 and 65
num_adult = 24370900

# Number of adults with age over 65
num_senior = 3730500 

# Number of citizens under 16 years old
num_child = 8342020 

# number of children (age < 16) per each 100 working adults (age 15-64)
child_dependency = 100 *(num_child / num_adult)

# number of seniors (age > 65) per each 100 working adults (age 15-64)
senior_dependency = 100 * (num_senior / num_adult)

# Calculation Part 
# 20 * num_adult
lazy = (20 * num_adult)
lazy2 = (1.5 * num_senior)

if senior_dependency <30 :
    if child_dependency <16:
        res = (40 * num_child)  + (40 * lazy2) + lazy

    elif child_dependency <65:
        res = (30 * num_child)  + (30 * lazy2) + lazy

    else :
        res = (20 * num_child) + (20 * lazy2) + lazy

elif senior_dependency >= 30:
    if child_dependency <=16:
        res = (50 * num_child) + (50 *lazy2)  + lazy
    else:
        res = (30 * num_child) + (30 * lazy2)  + lazy

print("Child Dependency Ratio:", round(child_dependency,2))
print("Senior Dependency Ratio:",round(senior_dependency,2))
print("Total aid the municipality receives is", res, "TL")


