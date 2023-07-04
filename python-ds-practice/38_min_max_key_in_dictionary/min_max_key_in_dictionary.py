import doctest
def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    #I didnt understand this one at first
    #at first read as two maxes but it is min and max
    # further more asks to evaluate keys not values
    # just had to create a list of keys with .keys() then call min and max which evaluates any type. nums are easiest and strings i think are by first character.
    keys = d.keys()

    return (min(keys), max(keys))

doctest.testmod(name='min_max_keys', verbose=True)
