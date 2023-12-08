import math


def main():
    print("Welcome to my first python calculator!")
    num1=float(input("Enter the first number: "))
    operation=input("Enter the operation(+, -, *, /, %, square, root, factorial, log): ")
    num2=float(input("Enter the second number: "))

    if operation == '+':
        print("Result: ", add(num1, num2))
    elif operation == '-':
        print("Result: ", subtract(num1, num2))
    elif operation == '*':
        print("Result: ", multiply(num1, num2))
    elif operation == '/':
        print("Result: ", divide(num1, num2))
    elif operation == '%':
        print("Result: ", modulus(num1, num2))
    elif operation == 'square':
        print("Result: ", square(num1))
    elif operation == 'root':
        print("Result: ", square_root(num1))
    elif operation == 'factorial':
        print("Result: ", factorial(num1))
    elif operation == 'log':
        print("Result: ", logarithm(num1, num2))
    else:
        print("Invalid operation. Please try again!")
        
def add(num1,num2):
    result = num1 + num2
    return result

def subtract(num1,num2):
    result = num1 - num2
    return result

def divide(num1, num2):
    if num2==0:
        print("Denominator is zero")
        result = print("Please try again")
    else:
        result = num1 / num2
        return result
#need to add divide by zero exception and return.
#also need to add return to start for repeat calculations

def multiply(num1, num2):
    result = num1 * num2
    return result

#modulus
def modulus(num1, num2):
    result = num1 % num2
    return result

#square (use second number to estimate square)
def square(num1):
    result = num1*num1
    return result


#square_root (use second number to estimate root)
def square_root(num1):
    num = int(num1)
    result = math.sqrt(num)
    return result

#factorial (use second number to estimate how many will result)
def factorial(num1):
    num = int(num1)
    if num == 1:
        return num
    else:
       return num* factorial(num-1)

#logarithm function where num1=base and num2=number to iterate
def logarithm(num1, num2):
    result = math.log(num2, num1)    
    return result

#call main function
main()
