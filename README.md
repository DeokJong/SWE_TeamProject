# 간단한 CUI 계산기

사용자가 입력한 계산식을 처리하고 결과를 출력하는 간단한 CUI 기반 계산기입니다.<br>
사용자는 키보드의 (+),(-),(*)를 이용하여 더하기, 빼기, 곱하기 연산을 수행할 수 있습니다.<br>
한 번의 입력에는 한 종류의 연산만 가능하며, 사용자가 '='를 입력하면 최종 결과가 출력됩니다.<br>
이 외의 입력이 들어온 경우 에러 메시지를 출력합니다.

## 개발환경
- python 3.x

## 예시
    15
    -
    3
    -
    10
    = 2

## 지원 연산
- 더하기 (+)
        
        addition_function(expression : str) -> int

- 빼기 (-)

        subtraction_function(expression)

- 곱하기 (*)
        
        multiplication_function(expression: str) -> int

## 제한 사항
- 피연산자는 정수만 가능합니다.
- 한 종류의 연산만 가능합니다.

## 이스터에그
만약 사용자가 특정 숫자를 입력하면 이스터에그 함수를 호출하여 특별한 메시지를 출력합니다.

    easteregg_function(variable)



## 계산식 유효성 검사
계산식이 유효한지 확인하기 위해 다음의 함수를 수행합니다.

    is_valid_expression(expression : str) -> bool