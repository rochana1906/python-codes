operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

def calculator():

    should_continue = True
    num1 = float(input("What is the first number?: "))

    while should_continue:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the second number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )

        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()
