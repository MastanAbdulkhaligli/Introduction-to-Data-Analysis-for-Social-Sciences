"""Mastan Abdulkhaligli 
21403007
CS
Lab05"""

# Part 2
sentence = input("Enter a sentence: ")

count = 0
for item in range(len(sentence)):
    if(sentence[item].isalpha()):
        count=count+1
    else:
        break

print("There are",count, "characters before a non-alphabetic character")