# Prime Number: Write a Python function that checks whether a given number is a prime number.

number = int(input("Enter your testing number: "))

def primeCheck(number):
    if number <= 1:
        return False
    for i in range(2,number + 1):
        if (number % i == 0):
            return False
    return True

print(primeCheck(number))
