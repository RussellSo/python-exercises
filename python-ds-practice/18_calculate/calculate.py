import doctest


def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """

    if operation == "add":
        return F"{message} {a + b}"

    if operation == "subtract":
        if make_int:
            return F"{message} {int(a - b)}"
        return F"{message} {a - b}"

    if operation == "multiply":
        return F"{message} {a * b}"

    if operation == "divide":
        return F"{message} {a / b}"

    # interesting concept
    # if another variable is true then change resulting variable
    # then return the whole thing
    # if make_int:
    #     res = int(res)

    # return f"{message} {res}"


doctest.testmod(name='calculate', verbose=True)
