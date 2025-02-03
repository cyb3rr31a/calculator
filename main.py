# A simple calculator that can add, subtract, multiply, and divide two numbers.

from art import logo

# Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("Enter first number: "))
                 
    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation: ")

        num2 = float(input("Enter next number: "))
        answer = operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {operations[operation](num1, num2)}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()