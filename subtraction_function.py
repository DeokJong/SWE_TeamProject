# 조훈희 담당
# 20231109 1차 작성
# 뺄셈 기능


def subtraction_function(expression):
    # expression은 식이란 뜻으로 사용.
    # 받는식은 띄어쓰기 없이 한줄로 string으로 입력받으려 한다.
    # example: 5-2=, 5-6-1=
    expression = expression.strip('=')
    # expression의 마지막 '='를 우선적으로 제거한다.
    array_of_expression = expression.split('-')
    # array_of_expression은 위의 식을
    # '-'를 기준으로 잘라서 만든 int Array 배열이다.
    result = int(array_of_expression[0])
    # 첫 array_of_expression의 값을 result로 정하고
    # for문을 사용하여 계산할 것이다.
    for component in array_of_expression[1:]:
        result -= int(component)
    return result


#밑은 subtract_function을 main으로 사용했을 때의 코드다.
#input_str = input("입력: ")
#if '=' in input_str:
#    result = subtract_function(input_str)
#    print("결과:", result)
#else:
#    print("error: incomplete expression")
