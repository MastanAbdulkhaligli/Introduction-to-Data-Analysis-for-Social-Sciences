"""Mastan Abdulkhaligli
CS 21403007
Lab 04  """

# Part 2
# Getting inputs from user 
width = float(input("Enter width:"))
height = float(input("\nEnter height:"))

area = width * height

 # Like a pro  (Killing readibility :D )
res = "Area = " + str(area) if area>=1000 else "Not big enough to build a farm."
print(res)


# What you want 
"""# If area is bigger and equal to 1000
if(area>=1000):
    print("Area =",area)
# if area less than 1000
else:
    print("Not big enough to build a farm.")"""