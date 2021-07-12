data = {'pencil': (2.40,5/100),
        'eraser': (4.5,10/100),
        'sharpener': (7.80,20/100),
        'crayon': (3.00, 10/100),
        'notebook':(8.60,25/100)}


print(data)

item1 = input("Enter an item name:")
price_item1 = data[item1][0] * (1-data[item1][1]) 

item2 = input("Enter an item name:")
price_item2 = data[item2][0] * (1-data[item2][1]) 

item3 = input("Enter an item name:")
price_item3 = data[item3][0] * (1-data[item3][1]) 

print("Total price to pay:", (price_item1+price_item2+price_item3))


