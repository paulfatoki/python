# functions
def check_sum(a,b,c):
    
    total = a + b + c 
    print(total)
    if total > 50:
        return "Yes > 50"
    else:
        return "No < 50"

# test the function with the numbers 10,20,30
result = check_sum(10,20,30)
print(result)
