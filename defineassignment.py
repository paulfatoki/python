def calculate_sum():
    
    #prompt the user to enter the first numeber
    
    first_number = input("Enter the first number:")
    
    # convert the user inputto a numeric type (float)
    
    first_number = float(first_number)
    
    
    #prompt the user the second number
    second_number = input( "Enter the secondnumber:")
    
    # convert the user input to numeric type (float)
    
    second_number = float(second_number)
    
    #calculate the sum of the two numbers
    
    total = first_number + second_number
    
    # check if the sum is greater than 100
    
    if total > 100:
        print(f"the sum is (total), which is large.")
    else:
        print(f"the sum is (total).")
        
        #call the function to execute the program
        calculate_sum
