
def add(a, b):
    """ Adds two numbers """
    return a + b


def subtract(a, b):
    """ Subtracts a number to another """
    return a - b


def multiply(a, b):
    """  Multiplies two numbers """
    return a * b


def divide(a, b):
    """ Divide two numbers """
    if b == 0:
        raise ValueError('Can not divide by zero.')
    return a / b


def calculate(calc):
    """ Interpret calculation """
    data = calc.split()
    if len(data) != 3:
        raise ValueError('Incorrect number of arguments.')
    a, method, b = data
    if not a.isnumeric() and b.isnumeric():
        raise ValueError('Not numeric values.')
    # Cast numeric values
    a = int(a)
    b = int(b)
    available_methods = ['+', '-', '*', '/']
    if method not in available_methods:
        raise ValueError('Bad method.')
    elif method == '+':
        return add(a, b)
    elif method == '-':
        return subtract(a, b)
    elif method == '*':
        return multiply(a, b)
    else:
        return divide(a, b)


if __name__ == '__main__':
    result = calculate("10 ! 5")
    print(result)
