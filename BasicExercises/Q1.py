#    Question 1 

counter  = 0
for item in range(280,3501):
    if((item%7 ==0) and (item%4==0)):
        counter = counter+1
        print(item)

print("The number of divisible by 7 and 4 is: ", counter)



        