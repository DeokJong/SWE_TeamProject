def get_variable():
    variable = input()
    return variable
def is_valid_variable(counter,variable):
    if(is_odd(counter)):
        return variable.isdigit()
    else:
        return is_operator(variable) 
def is_operator(operator):
    if(operator == "+" or
       operator == "-" or
       operator == "*" or
       operator == "=" ): return True
    else : return False
def is_odd(counter):
    if(counter%2==1):
        return True
    else:
        return False
def operate(number1,number2,operator):
    if(operator=="+"): return add_two_number(number1,number2)
    elif(operator=="-"): return number1-number2 # implement subtraction function
    elif(operator=="*"): return number1*number2 # implement multiple function
def add_two_number(number1,number2):
    return number1+number2
def is_done(varialbe):
    if(varialbe=="="): return True
    else : return False
def same_last_operator(current_operator,last_operator):
    if(last_operator==current_operator): return True
    else: return False
def detected_error():
    print("ERROR!")
    exit(1)

def main():
    number = None
    last_operator=None
    counter = 1

    while(True):
        variable = get_variable()
        if(not is_valid_variable(counter,variable)): detected_error()

        if(is_done(variable)):
            print(number)
            print("Done!")
            break

        if(is_odd(counter)):
            if(counter == 1):
                number=int(variable)
            else: number=operate(number,int(variable),last_operator)
            counter+=1
        else:
            if(last_operator==None): last_operator=variable

            if(same_last_operator(variable,last_operator)): counter+=1
            else: detected_error()

main()


