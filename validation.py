# 201812160 이재윤
# 유효성 검사 구현

def is_integer(variable: str) -> bool:
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


def is_valid_operator(operator: str) -> bool:
    """
    매개변수로 들어온 문자열이 유효한 연산자인지 확인합니다.

    Parameters:
    - operator (str) : 문자열

    Returns:
    - bool : 문자열이 유효한 연산자 (+, -, *)이면 True, 그렇지 않으면 False.
    """
    if operator in ('+', '-', '*', '!') :
        return True
    else :
        return False


def is_valid_expression(expression: str) -> bool:
    """
    매개변수로 들어온 계산식이 유효한 계산식인지 확인합니다.

    Parameters:
    - expression (str) : 계산식

    Returns:
    - bool : 계산식이 유효하면 True, 그렇지 않으면 False.
    """

    currentOperator: str = ""
    tokens = expression.split(" ")  # list

    for i in range(len(tokens)):
        if i % 2 == 0:  # 피연산자 위치
            if not is_integer(tokens[i]):
                print_error_message()
                return False

        else:  # 연산자 위치
            if not is_valid_operator(tokens[i]):
                print_error_message()
                return False

            if currentOperator == "":
                currentOperator = tokens[i]

            elif currentOperator != tokens[i]:
                print_error_message()
                return False

        if currentOperator == "!":
            if len(tokens) != 2:
                print("[Error] Input Error")
                return False
            if int(tokens[0]) < 0:
                print("[Error] Out Of Range")
                return False

    return True


def print_error_message() -> None:
    """
    유효하지 않은 계산식인 경우 오류 메시지를 출력합니다.
    """
    print("[ERROR] Input Error")


def getOperator(expression: str) -> str:
    tokens = expression.split(" ")
    return tokens[1]
