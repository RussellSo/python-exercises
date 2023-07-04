import doctest
def compact(lst):

    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newLst = []

    # for thing in lst:
    #     if True:
    #         newLst.append(thing)
    # return newLst

    #append val - first lets set val to iterate through list, only append val if val is a true item)
    return [val for val in lst if val]
doctest.testmod(name='compact', verbose=True)
