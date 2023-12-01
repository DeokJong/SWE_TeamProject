# 201918351 장정우
# 코드 파트 별 통합

from addition_function import addition_function  # 진덕종 파트
from subtraction_function import subtraction_function  # 조훈희 파트
from Multiplication_function import multiplication_function  # 니키 파트
from validation import is_valid_expression, print_error_message, getOperator  # 이재윤 파트
from easteregg_function import easteregg_function  # 김혜정 파트


def calculator():
    expression = ""
    result = None

    while True:
        user_input = input("User input: ")
        easteregg_function(user_input)

        # 입력값이 '='일 경우 연산 시작
        if user_input == '=':
            expression = expression.rstrip()#문자열의 공백 제거

            #유효성 검사 성공하면 연산 시작
            if is_valid_expression(expression):
                operator = getOperator(expression)

                if operator == "+":
                    result = addition_function(expression)
                elif operator == "-":
                    result = subtraction_function(expression)
                elif operator == "*":
                    result = multiplication_function(expression)
                elif operator == "!":
                    result = 10000000

                if result is not None:
                    print("output:", result)
                break

            else:
                print_error_message()
                break
        # 입력값이 '='이 아닐 경우
        else:
            expression += user_input
            expression += " "


if __name__ == "__main__":
    calculator()
