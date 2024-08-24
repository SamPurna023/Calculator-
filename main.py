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
    "/": divide,
}

#print(operations["*"](4, 6))

def calculator():
    from art import logo
    print(logo)
    should_accumulate = True
    first_number = float(input("What is the First number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        select_operation = input("Pick an operation: ")
        next_number = float(input("What is the next number?: "))
        answer = operations[select_operation](first_number, next_number)
        print(f"{first_number} {select_operation} {next_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation:")
        if choice == "y":
            first_number = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()