#201910083_니키 

def calculate_product():
    # multiplication problem
 
    user_input = input("Input a multiplication problem: ")

    if ' times ' in user_input:
        # Extract the numbers 
        operand1, operand2 = map(int, user_input.split(' times '))

        # calculate 
        result = operand1 * operand2
        print("The result of multiplying {} and {} is: {}".format(operand1, operand2, result))
    else:
        print("Wrong input")
