import doctest
def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

   #iterate through keys
   # add to dict with value pair

    new_dict = {}

    #had to look at solution for enumerate function
    #enumrate allows of idx be available
    for idx, val in enumerate(keys):
        #first part is saying, keys and idx go hand in hand so dict of keys will equal value of idx.
        # thats if current key idx is less than current value idx
        #if current key is present and no value is present than the value will equal none
        new_dict[val] = values[idx] if idx < len(values) else None
    return new_dict



doctest.testmod(name='two_list_dictionary', verbose=True)
