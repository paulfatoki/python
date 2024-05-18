# doubleloop2
basket = []
for x in [3,4,5]:
    for y in [3,1,4]:
        if x != y:
            basket.append((x, y))
            
print(basket)