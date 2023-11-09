def is_integer(variable : str) -> bool:
    try:
        int(variable)
        return True
    
    except ValueError:
        return False
    
def is_valid_operator(operator : str) -> bool:
   return operator in ('+', '-', '*', '=')


def is_valid_expression(num1 : str, operator : str, num2 : str) -> bool:
    return is_integer(num1) and is_valid_operator(operator) and is_integer(num2)
       
def print_error_message() -> None:
    print("ERROR")
