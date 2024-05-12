list1=[1,2,4,6,7,9,10,11,13,14]
x = 1
for i in list1:
    x = x * i
    print(x/1000)
    if x >100:
        break
        print('final result')
    