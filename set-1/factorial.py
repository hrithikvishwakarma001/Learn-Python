# Factorial Calculation: Write a Python function that calculates the factorial of a number.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return f"Factorial of {n} is {result}."

# Test the function with the input 5
print(factorial(5))
