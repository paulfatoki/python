# animals
animals=["Yes",  "Yes", "Yes", "No","Yes", 
        "Yes", "Yes","Yes","Yes", "No",
        "Yes", "No", "Yes", "No",   "No", 
        "Yes","Yes", "Yes", "Yes", "Yes",
        "No",  "No",  "Yes","Yes", "No",
        "Yes"]
# create empty count
cowcount = 0
cowpresent = []
for i in animals:
    #print(i)
    if i == 'Yes':
        cowcount = cowcount = 1 
        cowpresent.append(i)
        print(cowpresent)
    else:    
        continue
print(cowpresent.count(i))

        