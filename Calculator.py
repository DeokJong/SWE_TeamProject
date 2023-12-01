# 201918351 장정우
# 코드 파트 별 통합

from addition_function import addition_function # 진덕종 파트
from subtraction_function import subtraction_function # 조훈희 파트
from Multiplication_function import multiplication_function # 니키 파트
from validation import is_valid_expression, print_error_message, getOperator # 이재윤 파트
from easteregg_function import easteregg_function # 김혜정 파트

def calculator():
    expression = ""
    
    while True:
        user_input = input("User input: ")
        easteregg_function(user_input)
        expression += user_input
        expression += " "

        if user_input == '=':
            if len(expression) <= 6 and '!' not in expression:
                print_error_message()
                break

            if is_valid_expression(expression):
                operator = getOperator(expression)

                if operator=="+":
                    result = addition_function(expression)
                elif operator=="-":
                    result = subtraction_function(expression)
                elif operator=="*":
                    result = multiplication_function(expression)
                elif operator=="!":
                    result = 10000000
                    
                if result is not None:
                    print("output:", result)
                break

            else:
                print_error_message()
                break

if __name__ == "__main__":
    calculator()
