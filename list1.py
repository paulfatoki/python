list1=[1,2,4,6,7,9,10]
threshold = 13
basket=[]
basket2=[]
x = 0
for i in list1:
    x = x + i
    #print(x)
    print('This is another senario' )
    if x < 13:
        basket2.append(x)
        print(basket2)
        #break
    else:
     if x > 13:
        basket.append(x)
        print(basket)
        
        
        