#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
   print (parameter)

   return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
   numbers = ''

   for number in range(int(parameter)):
       numbers += f'{number}\n'

   return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
        return str(result)
    elif operation == '-':
        result = num1 - num2
        return str(result)
    elif operation == '*':
        result = num1 * num2
        return str(result)
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
            return str(result)
        else:
            return 'Division by zero is not allowed.'
    elif operation == '%':
        result = num1 % num2
        return str(result)
    else:
        return 'Invalid operation. Supported operations are: +, -, *, div, %'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

