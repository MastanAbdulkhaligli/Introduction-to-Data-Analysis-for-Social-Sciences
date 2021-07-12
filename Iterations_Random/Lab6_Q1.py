"""Mastan Abdulkhaligli
Lab06
21403007 CS"""

# Part 1 

# Our data
data = {'coral pink':[1,'gallon'],
        'sage green':[0.5,'gallon'],
        'ice blue':[3,'L']}


color = input("Enter paint to search: ")

if color in data:
    number_of_rooms = int(input("Enter number of rooms: "))
    need = number_of_rooms * data[color][0]
    print("You will need", need, data[color][1], "of ", color)
else:
    print(color,"is not in the paint list.")