"""Mastan Abdulkhaligli 
21403007
CS
Lab05"""

# Part 1 


# Part a)
initial_case = 5370299
start = 5370299
decrease_rate = 6.16/100
increament_rate = 6.7/100

for item in range(10):
    initial_case = initial_case * (1-decrease_rate)
    decrease_rate = decrease_rate * (1 + increament_rate)
    print("Total cases in week 26 of 2021: ",round(initial_case))

print("""Total decrease in Covid19 cases:""",round(start - initial_case))


# Part b)
initial_case = 5370299
decrease_rate = 6.16/100
increament_rate = 6.7/100
week = 25

# The reason i put 25 as a range is starting week is 25. Minus week is not possible 
for item in range (25):
    initial_case = initial_case * (1-decrease_rate)
    decrease_rate = decrease_rate * (1 + increament_rate)
    week = week +1
    if(initial_case <1000000):
        break

print("Covid19 case count will fall below 1000000 in week ",week, "Cases: ", round(initial_case))



# Actually we do not know how many iterations will happen to reach 1000000 that is why first i used while loop
"""initial_case = 5370299
decrease_rate = 6.16/100
increament_rate = 6.7/100
week = 25
while(initial_case > 1000000):
    initial_case = initial_case * (1-decrease_rate)
    decrease_rate = decrease_rate * (1 + increament_rate)
    week = week +1

print("Covid19 case count will fall below 1000000 in week ",week, "Cases: ", round(initial_case))"""
