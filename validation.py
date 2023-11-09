# 201812160 이재윤
# 유효성 검사 구현 

def is_integer(variable : str) -> bool:
    """
    매개변수로 들어온 문자열이 정수인지 확인합니다.

    Parameters:
    - variable (str) : 문자열

    Returns:
    - bool : 문자열이 유효한 정수이면 True, 그렇지 않으면 False.
    """
    
    try:
        int(variable)
        return True
    
    except ValueError:
        return False
    
def is_valid_operator(operator : str) -> bool:
    """
    매개변수로 들어온 문자열이 유효한 연산자인지 확인합니다.

    Parameters:
    - operator (str) : 문자열

    Returns:
    - bool : 문자열이 유효한 연산자 (+, -, *, =)이면 True, 그렇지 않으면 False.
    """
   
    return operator in ('+', '-', '*', '=')


def is_valid_expression(num1 : str, operator : str, num2 : str) -> bool:
    """
    매개변수로 들어온 계산식이 유효한 계산식인지 확인합니다.

    Parameters:
    - num1 (str) : 첫 번째 피연산자.
    - operator (str) : 연산자
    - num2 (str) : 두 번째 피연산자.

    Returns:
    - bool : 계산식이 유효하면 True, 그렇지 않으면 False.
    """
    
    return is_integer(num1) and is_valid_operator(operator) and is_integer(num2)
       
def print_error_message() -> None:
    """
    유효하지 않은 계산식인 경우 오류 메시지를 출력합니다.
    """
    print("ERROR")