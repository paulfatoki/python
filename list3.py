list1=[1,2,4,6,7,9,10]
threshold=29
collate=[]
x = 0 
for i in list1:
    x = x + i
    if x < threshold:
     collate.append(x)
     print(collate)
     
     