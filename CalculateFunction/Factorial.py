def factorial(expression : str) -> int:
    expression_list = expression.split(" ")
    max_number = int(expression_list[0])
    result = 1

    while max_number != 0:
        result *= max_number
        max_number -= 1

    return result
