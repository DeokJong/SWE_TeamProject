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
        easteregg_function(user_input)
        expression += user_input

        if user_input == '=':
            if len(expression) <= 3:
                print_error_message()
                break

            if is_valid_expression(expression):

                if expression.find('+') != -1:
                    result = addition_function(expression)
                elif expression.find('-') != -1:
                    result = subtraction_function(expression)
                elif expression.find('*') != -1:
                    result = multiplication_function(expression)
                
                if result is not None:
                    print("output:", result)
                break

            else:
                print_error_message()
                break

if __name__ == "__main__":
    calculator()
