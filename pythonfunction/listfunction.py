# write a python function that will iterate through a list of items
list1 = [1, 5, 10, 20, 30, 40, 50 , 60]
def loop():
    #list1 = [1, 5, 10, 20, 30, 40, 50 , 60]
    for i in list1:
        #print(i)
        # check if the sum of list1 is than 500
        total = sum(list1)
        if total < 50:
            hurray()
            break
        else:
            ohno(total)  
            break          
def hurray():
    print('yes it is lesser 500')
    
def ohno(tot):
    result = tot * 20
    print('my final result:' + str(result))
    
    

        
    
     # calling the function       
loop()
    


    
    
        
        