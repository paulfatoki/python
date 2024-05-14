# market items and their prices using input code method
#listofitems= ('Yam for 200', 'cassava for 300', 'groundnut oil for 500' , 'meat for 1000' , 'maize for 300')

# input coding 
items = { "Yam": int(input("Enter the price of Yam")),
        "Cassava": int(input("Enter the price of Cassava")),
        "Groundnut oil": int(input("Enter the price of Groundnut oil")),
        "Meat": int(input("Enter the price of Meat")),
        "Maize":int(input("Enter the price of Maize"))
        }

#calculate the sum of the amounts

total_amount = sum(items.values())

#Print the sum and the items in deatil

print("Total Amount:" , total_amount)
print("items:")
for item, price in items.items():
    print("{item}: {price}")