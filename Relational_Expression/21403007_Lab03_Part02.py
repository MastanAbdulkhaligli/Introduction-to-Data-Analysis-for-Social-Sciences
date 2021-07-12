"""Mastan Abdulkhaligli
21403007 CS
Lab 03"""

# Part 2
# User enter sentence and this sentence assigns to var "sentence"
sentence = input("Enter a sentence (including spaces before/after):")

# Print original sentence
print("Original Sentence: ",'"'+ sentence + '"')

# Removing first and last space from sentences
sentence = sentence.strip()
print("After Stripping Sentence: ",'"'+ sentence + '"')

# replace all letters 'e' with '*#*'
sentence = sentence.replace('e','*#*')
sentence = sentence.replace('E','*#*')
print("After replacements:" + '"' + sentence + '"')

# count the number of replacements made
print(sentence.count('#'),"replacements made")

# finds and displays the substring starting from the first '*' of the first replacement and ending
# at the last '*' in the last replacement 

# First *
s1= sentence.find('*')
print("s1:",s1)

# Last *
s2 = sentence.rfind('*')
print("s2:",s2)

# Printing substring
print("Substring:" + '"' + sentence[s1:s2+1] + '"')


