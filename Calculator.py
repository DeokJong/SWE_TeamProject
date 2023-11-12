# 201918351 장정우
# 코드 파트 별 통합

from addition_function import addition_function # 진덕종 파트
from subtraction_function import subtraction_function # 조훈희 파트
from Multiplication_function import multiplication_function # 니키 파트
from validation import is_valid_expression, print_error_message # 이재윤 파트
from easteregg_function import easteregg_function # 김혜정 파트

def calculator():
    expression = ""
    
    while True:
        user_input = input("User input: ")
        expression += user_input

        if user_input == '=':
            if len(expression) <= 2:
                print("ERROR")
                break

            if is_valid_expression(expression):

                operator = expression[1]

                if operator == '+':
                    result = addition_function(expression)
                elif operator == '-':
                    result = subtraction_function(expression)
                elif operator == '*':
                    result = multiplication_function(expression)
                
                if result is not None:
                    print("output:", result)
                break

            else:
                print_error_message()
                break

        elif easteregg_function(user_input):
            break

if __name__ == "__main__":
    calculator()
