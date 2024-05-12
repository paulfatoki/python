# Write a python code that will add list of numbers together
list1=[1,2,4,6,7,9,10]
x = 0
for i in list1:
    #print(i)
    
    x = x + i
    print(x)
    if x == 13:
        y = (x * 50 / 100) - 200
        print('this is my final result ' + str(y)) 
        break 
    else:
        continue