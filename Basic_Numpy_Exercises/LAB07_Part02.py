# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 18:02:41 2021

@author: Mastan Abdulkhaligli
"""
import numpy as np 
# Initialize two one dimensional arrays
PlayerA = np.random.randint(0,11,8) # np.array([5,10,7,4,9,6,10,1])
PlayerB = np.random.randint(0,11,8)#np.array([5,6,3,4,2,4,9,4])

print(PlayerA)
print(PlayerB)

# Calculate and display the number of tournaments PlayerA had a better performance.
print("\nPlayer A has performed better in",sum(PlayerA > PlayerB), "tournaments")

#  Display the scores of the tournaments that PlayerB had a poorer performance
print("Scores for player B performing poorer:",(PlayerB[PlayerB < PlayerA]))

# Calculate the maximum matches won in a tournament for PlayerA.
print("Maximum score for Player A:", max(PlayerA))

# Calculate the average matches won for all tournaments
print("Average score (all tournaments): ", np.mean(np.concatenate((PlayerA,PlayerB))))

#. Calculate the point spread
print("Point difference for each tournament:",abs(PlayerA-PlayerB))

# Display the set number for tournaments that were tied
print((np.where(PlayerA==PlayerB))[0]+1)



