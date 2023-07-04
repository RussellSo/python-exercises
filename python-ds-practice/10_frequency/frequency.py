import doctest
def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    #.count is a lst function
    return lst.count(search_term)

doctest.testmod(name='frequency', verbose=True)
