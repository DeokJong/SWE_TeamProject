# 201916136 조훈희
# implementation Subtraction_function
#
# First, remove '='.
# second, divide expression to make number list
# third, sub all the numbers in the list of numbers
# fourth, return result

def subtraction_function(expression: str) -> int:
    number_list = expression.split(" - ")  # divide expression to make list

    result = int(0)  # initiate reslut variable

    for number in number_list:  # sum number repeatedly
        result += int(number)

    return result
