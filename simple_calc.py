def is_number(prompt):
    while True:
        user_input = input(f'{prompt}: ')
        try:
            return float(user_input)
        except ValueError:
            print('Please enter a valid number.')

num1 = is_number('first digit')
num2 = is_number('second digit')
operation = input('enter the operation sign: ')

def calculations(num1, num2, operation):
    if operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else 'trying to divide by 0'
    elif operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation in ['^', '**']: #same as operation == ** or operation == ^
        return num1 ** num2
    else:
        print ('Invalid operation')

result = calculations(num1, num2, operation)
print('Result:', result)
