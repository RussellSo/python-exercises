import doctest
def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    

    # iterate through phrase
    # if conditional then REASSIGN the iteratable to be swapcase 
    # then += iterable into new string whether it meets conditional or not
    # great way to use condition to just change the iterable rather than change anything else
    final = ""

    for ltr in phrase:
        if ltr.lower() == to_swap.lower():
            ltr = ltr.swapcase()
        final += ltr
    return final


doctest.testmod(name='flip_case', verbose=True)
