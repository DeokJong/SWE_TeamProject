#201910083_니키 
# Implementation of multiplication_function
# divide expression to make a list of numbers.
# multiply all the numbers in the list of numbers.
# return the result.

def multiplication_function(expression: str) -> int:
    expression = expression.strip('=')  # Remove '='
    number_list = expression.split('times')  # Divide expression to make a list

    result = 1  # Initialize result variable to 1 for multiplication

    for number in number_list:  # Multiply numbers repeatedly
        result *= int(number)

    return result

