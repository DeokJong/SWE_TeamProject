# 201918351 장정우
# 코드 파트 별 통합 최종본

def calculator():
    expression = ""
    
    while True:
        user_input = input("User input: ")
        expression += user_input

        if user_input == '=':
            if is_valid_expression(expression):

                operator = expression[1]

                if operator == '+':
                    result = addition_function(expression)
                elif operator == '-':
                    result = subtract_function(expression)
                elif operator == '*':
                    result = multiplication_function(expression)
                
                if result is not None:
                    print(result)
                break
            else:
                print_error_message()
                break

        elif easteregg_function(user_input):
            print("lucky number!")
            break

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
    - bool : 문자열이 유효한 연산자 (+, -, *)이면 True, 그렇지 않으면 False.
    """
   
    return operator in ('+', '-', '*')


def is_valid_expression(expression : str) -> bool:
    """
    매개변수로 들어온 계산식이 유효한 계산식인지 확인합니다.

    Parameters:
    - expression (str) : 계산식

    Returns:
    - bool : 계산식이 유효하면 True, 그렇지 않으면 False.
    """
    
    currentOperator:str = ""
    count = 0

    for i in range(len(expression) - 1):
        if count % 2 == 0:
            if not is_integer(expression[i]):
                return False
            
        else:
            if not is_valid_operator(expression[i]):
                return False
        
            if currentOperator == "":
                currentOperator = expression[i]

            elif currentOperator != expression[i]:
                return False

        count += 1

    if expression[-1] != "=":
        return False
        
    return True

def print_error_message() -> None:
    """
    유효하지 않은 계산식인 경우 오류 메시지를 출력합니다.
    """
    print("ERROR!")

def easteregg_function(user_input): # 이스터에그 처리
    if user_input == "777":
        return True

def addition_function(expression) -> int: # 덧셈 연산 수행
    expression = expression.strip('=') #remove '='
    number_list = expression.split('+') #divide expression to make list

    reslut = int(0) # initiate reslut variable
    for number in number_list: # addition
        reslut += int(number)

    return reslut 

def subtract_function(expression) -> int: # 뺄샘 연산 수행
    expression = expression.strip('=') #remove '='
    number_list = expression.split('-') #divide expression to make list

    reslut = int(number_list[0]) # initiate reslut variable
    
    for number in number_list[1:]: # subtract
        reslut -= int(number)

    return reslut 

def multiplication_function(expression) -> int: # 곱셈 연산 수행
    expression = expression.strip('=') #remove '='
    number_list = expression.split('*') #divide expression to make list

    reslut = int(1) # initiate reslut variable
    
    for number in number_list: # multiplication
        reslut *= int(number)

    return reslut 

if __name__ == "__main__":
    calculator()
