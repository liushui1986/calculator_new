from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return 0
    else:
        return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    num1 = float(input('Please write down your first number: \n'))
    continue_go = 'y'

    while continue_go == 'y':
        for symbol in operations:
            print(symbol)
        operator = input('Please choose an operator: \n')
        num2 = float(input('Please write down the second number: \n'))

        result = operations[operator](num1, num2)
        print(f'The result is : {num1} {operator} {num2} = {result}')

        continue_go = input('Do you want to use your current result (Y/N)?\n').lower()
        if continue_go == 'y':
            num1 = result
        else:
            print('\n' * 100)
            calculator()


calculator()
