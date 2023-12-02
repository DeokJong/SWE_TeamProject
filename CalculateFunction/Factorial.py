# 201916136 Deokjong Jin
# implementation Factorial_function
#
# First, remove '='.
# second, divide expression to make number list
# third, calculate factorial
# fourth, return result

def factorial(expression: str) -> int:
    number_list = expression.split(" ")
    max_number = int(number_list[0])
    result = 1

    while max_number != 0:
        result *= max_number
        max_number -= 1

    return result
