def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

def calculator():
    print("Functional Calculator")
    print("Operations: +, -, *, /")
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    if operation == '+':
        print("Result:", add(a, b))
    elif operation == '-':
        print("Result:", subtract(a, b))
    elif operation == '*':
        print("Result:", multiply(a, b))
    elif operation == '/':
        print("Result:", divide(a, b))
    else:
        print("Invalid operation!")

# ფუნქციის გაშვება
calculator()