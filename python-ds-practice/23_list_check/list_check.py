import doctest
def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    # had to put the true return after the loop because we dont want to return true so quickly.
    for items in lst:
        if not isinstance(items, list):
            return False
    return True
doctest.testmod(name='list_check', verbose=True)
