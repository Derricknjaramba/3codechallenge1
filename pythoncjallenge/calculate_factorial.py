# calculate_factorial.py

def calculate_factorial(n):
    # Returns the factorial of the non-negative integer n
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1  # Factorial of 0 is 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
