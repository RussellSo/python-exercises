import doctest
def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    #if start then slice list
    #if find (osught)
    #-----
    # my thought process in slicing from start was good, and use of isistance was good
    # but how syntax works in python means i didnt go the right route with "finding" sought


    # if start and isinstance(collection, list):
    #     collection = collection[start:]
    
    # if isinstance(collection, list):
    #     if collection.find(sought):
    #         return True

    # if isinstance(collection, str):
    #     if range(str).find(sought):
    #         return True

    #specifyig dict because we have to find IN .values()
    if isinstance(collection, dict):
        return sought in collection.values()

    #works on sets/ i dont know why if start = None was added??
    if isinstance(collection, set):
        return sought in collection

    #looking at lists and strings and allows for start
    return sought in collection[start:]

    ##LEARNED THAT "IN" IS A POWERFUL FINDER
    ## LEARNED THAT EACH DATA STRUCTURE HAS MANY DIFFERENT RULES
    ## personally i think i would have gotten dict, but the others i would have flubbed with 


doctest.testmod(name='includes', verbose=True)
