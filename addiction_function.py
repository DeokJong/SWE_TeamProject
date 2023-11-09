#201916136 Deokjong Jin
#implementation addiction_function
#
#First, remove '='.
#second, divide expreesion to make number list
#third, sum all the numbers in the list of numbers
#fourth, return result

def addiction_function(expression : str) -> int:
    expression = expression.strip('=') #remove '='
    number_list = expression.split('+') #divide expression to make list

    reslut = int(0) # initiate reslut variable
    
    for number in number_list: # sum number repeatedly
        reslut+=int(number)

    return reslut 