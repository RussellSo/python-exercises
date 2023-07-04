import doctest

def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """

    return a * b

doctest.testmod(name='product', verbose=True)