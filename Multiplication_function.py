#201910083_니키 
# Implementation for multiplication_function
#
# First, check for '*'.
# Second, split the expression to create a list of numbers.
# Third, multiply all the numbers in the list.
# Fourth, return the result.

 def multiplication_function(expression: str) -> float:
    try:
        # Check for '*'
        if '*' in expression:
            
            num1, num2 = map(float, expression.split('*'))
            
            # Multiply the numbers
            result = num1 * num2
            print("Result:", result)
        
        else:
            print("Error: Invalid input.")
    
    except (ValueError, Exception) as e:
        print(f"Error: {e}")
multiplication_function(input("Enter a mathematical expression: "))
