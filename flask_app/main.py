from flask import Flask, render_template, request
from art import logo

app = Flask(__name__)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operator = request.form['operator']
            result = operations[operator](num1, num2)
        except (ValueError, KeyError):
            result = "Invalid input or operation."

    return render_template('index.html', logo=logo, result=result, num1=num1, num2=num2, operator=operator)

if __name__ == '__main__':
    app.run(debug=True)
