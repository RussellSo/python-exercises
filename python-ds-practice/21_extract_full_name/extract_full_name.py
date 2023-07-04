import doctest


def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    #need to use list comprehension - it works
    #List comprehension allows us to iterate through the names array and then interpolate the first key value and second key value
    #when interpolating using multiple quotes, have to use single for inner quotes

    return [F"{person['first']} {person['last']}" for person in people]


doctest.testmod(name='extract_full_name', verbose=True)
