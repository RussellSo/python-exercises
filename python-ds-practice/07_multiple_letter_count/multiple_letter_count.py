import doctest
def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # empty dict
    ltrcounts = {}

    for ltr in phrase: # iterate ltr times
        #create a key with ltrcounts[ltr]: 
        #use get to assign a default of 0, and also use + operator to keep adding as we iterate
        ltrcounts[ltr] = ltrcounts.get(ltr, 0) + 1

    return ltrcounts

doctest.testmod(name='multiple_letter_count', verbose=True)


