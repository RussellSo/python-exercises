import doctest
def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    #split sent
    # check len, if len is shorter than n
    # find difference
    # += ...

    ## I think whats happening is we're truncating by 3
    ## so we're slicing the phrase from start to number, and subtracting 3 to account for the ellipses
    # i actually have no idea - think that there's some logic here saying that the length of the phrase has to be greater than 3


    #start with edge case
    if n < 3:
        return "Truncation must be at least 3 characters."

    #second edge case
    if n > len(phrase) + 2:
        return phrase
    
    # the meat, slice from start to n - 3 for ellipses. add ellipses
    return phrase[:n - 3] + "..."

doctest.testmod(name='truncate', verbose=True)
