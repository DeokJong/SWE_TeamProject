# 201918351 장정우
# 코드 파트 별 통합

from addition_function import addition_function  # 진덕종 파트
from subtraction_function import subtraction_function  # 조훈희 파트
from Multiplication_function import multiplication_function  # 니키 파트
from validation import is_valid_expression, print_error_message, getOperator  # 이재윤 파트
from easteregg_function import easterEgg_function  # 김혜정 파트
from Factorial import factorial


def calculator():
    expression = ""
    operator = ""
    result = None

    while True:
        user_input = input()
        easterEgg_function(user_input)

        # (입력값이 '=' 또는 '!' 일 경우 연산 시작) or (식에다가 입력값 붙여넣기)
        if user_input == '=' or user_input == '!':
            expression = expression.rstrip()  # 문자열의 공백 제거
            if user_input == '!': expression += " !"  # 팩토리얼 인식을 위해 느낌표 붙이기

            # 유효성 검사 성공하면 연산 시작 그렇지 않으면 탈출.
            if is_valid_expression(expression, user_input):
                operator = getOperator(expression)

                if operator == "+":
                    result = addition_function(expression)
                elif operator == "-":
                    result = subtraction_function(expression)
                elif operator == "*":
                    result = multiplication_function(expression)
                elif operator == "!":
                    result = factorial(expression)

                if result is not None:
                    print(result)
                break

            else:
                if (user_input == '!'):
                    print_error_message(expression)

                else:
                    print_error_message()
                
                break
        # 입력값이 '='이 아닐 경우
        else:
            expression += user_input
            expression += " "


if __name__ == "__main__":
    calculator()
