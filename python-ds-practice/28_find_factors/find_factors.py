import doctest
def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    #interesting case
    #1: have to always use // in range because it can only accept integers
    #2: for this factorial function, for finding the range, the halfway number i.e. 5 for factorial 10 is not inclusive. so you have to always add "+1"

    listed = [n for n in range(1, num // 2 + 1) if num % n == 0]
    listed.append(num)
    return listed
    

doctest.testmod(name='find_factors', verbose=True)

