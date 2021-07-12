"""Mastan Abdulkhaligli
Lab06
21403007 CS"""
# Part 2 
import random 
# Long version of this code in below 
randomList = []
for f in range(0,12): randomList.append(random.randint(1000,10000))
print("Customer counts:",randomList)
print("Yearly Average Customer Count:",round(sum(randomList)/len(randomList)))
print("Maximum customer count was", max(randomList), "in week", randomList.index(max(randomList))+1)
print("Customer counts below average: ")
# Try to make code shorter *
below_avg = [x for x in (randomList) if x < round(sum(randomList)/len(randomList))]
[print(item) for item in below_avg]
print("Number of months with below average customer counts:", len(below_avg))



# Long version of generation random numbers
"""randomList = []
for i in range(0,12):
    n = random.randint(1000,10000)
    randomList.append(n)"""



# Long version of *
"""below_avg = []
for item in range(len(randomList)):
    if (randomList[item] < round(sum(randomList)/len(randomList))):
        below_avg.append(randomList[item])
        print(randomList[item])
print("Number of months with below average customer counts:", len(below_avg))"""



