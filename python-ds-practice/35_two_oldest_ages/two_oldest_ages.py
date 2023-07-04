import doctest
def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    #thought process - apparentl have to call a sorted(ages) function - then maybe add to a set and return tuple.
    #1
    set_ages = set(ages)
    #2 sort = sorted function returns a new list where sort function mutates the one in place
    oldest = sorted(set_ages)[-2:] # from second to last to end - still a set
    #3 return a tuple
    return tuple(oldest)
    # my solution was almost correct although i didnt know the syntax -
    # order was actually to turn list into a set, then call sorted on the list, and return tuples
    #LEARNING CASE: calling set on a list seems to be quite helpful

doctest.testmod(name='two_oldest_ages', verbose=True)
    