import doctest
def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

# works but i think we want to return true instead
    # if not lst:
    #     return None 

    # How does this return True if lst is None?
    if lst:
        return lst[-1]

doctest.testmod(name='last_element', verbose=True)
