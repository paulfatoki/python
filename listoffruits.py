#task 4 - a python code to determine duplicate
duplicatebasket=[]
emptybasket=[]
listoffruits=["banana" , "watermelon" , "carrot" , "carrot" , "pawpaw" , "orange", "banana"]
for i in listoffruits:
    
    #print(i)
    emptybasket.append(i)
    if emptybasket.count(i)> 1:
        duplicatebasket.append(i)
        print(duplicatebasket)

