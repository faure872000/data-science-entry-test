def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    #check if divisor is 0 to avoid errors
    if divisor == 0:
        return False
    #check if both num and divisor are numeric types
    elif isinstance(num, (int,float)) and isinstance(divisor, (int,float)):
        if num % divisor == 0:   
            return True
        else:
            return False
    else:
        return "Not numeric"


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
