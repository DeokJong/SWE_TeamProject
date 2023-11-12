def calculator():
    expression = []
    
    while True:
        user_input = input("User input: ")
            
        if user_input == '=':
            if is_valid_expession(expression):

                operator = expression[1]

                if operator == '+':
                    result = addition_function(expression)
                elif operator == '-':
                    result = subtract_function(expression)
                elif operator == '*':
                    result = multiplication_function(expression)
                
                if result is not None:
                    print("=", result)
                break
            else:
                print("= ERROR!")
                break

        elif easteregg_function(user_input):
            print("lucky number!")
            break

        else:
            expression.append(user_input)

def is_valid_expession(expression): # 입력 값 유효성 검사
    
    for i in range(0, len(expression), 2): # 정수 값 입력 확인
        if not expression[i].isdigit():
            return False
        
    current_operator = ""
    for i in range(1, len(expression), 2): # 연산자 확인 (사용가능한 연산자 + 하나의 연산자만 사용)

        if expression[i] not in {'+', '-', '*'}:
            return False
        
        if current_operator == "":
            current_operator = expression[i]
        elif current_operator != expression[i]:
            return False
        
    return True

def easteregg_function(user_input): # 이스터에그 처리
    if user_input == "777":
        return True

def addition_function(expression): # 덧셈 연산 수행
    result = 0
    for i in range(0, len(expression), 2):
        result += int(expression[i])
    return result

def subtract_function(expression): # 뺄샘 연산 수행
    result = 0
    for i in range(0, len(expression), 2):
        result -= int(expression[i])
    return result

def multiplication_function(expression): # 곱셈 연산 수행
    result = 1
    for i in range(0, len(expression), 2):
        result *= int(expression[i])
    return result

if __name__ == "__main__":
    calculator()
