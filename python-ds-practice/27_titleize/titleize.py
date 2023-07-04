import doctest
def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    #join function changes in python. need to call .join on an empty string " "
    # logic: empyt array. split existing string, iterate and add capitals, call join
    # soluton logic: [word.capitalize() for word in phrase.split] then call the join function on it.
    # sytax: add capitaled function into an array for every word in a splitted funciton.

    new_str = []
    split = phrase.split(' ')
    for word in split:
        new_str.append(word.capitalize())

    return " ".join(new_str)

    #easier solution would be
    # return phrase.title()

    
    



doctest.testmod(name='titleize', verbose=True)

