import doctest
# def freq_counter(coll):
#     """Returns frequency counter mapping of coll."""

#     counts = {}

#     for x in coll:
#         counts[x] = counts.get(x, 0) + 1

#     return counts


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    #my way
    counts_1 = {    }
    counts_2 = {}

        #how do i make pairs?
    num_str = str(num1)
    for num_a in num_str:
        counts_1[num_a] = counts_1.get(num_a, 0) + 1

    for num_b in str(num2):
        counts_2[num_b] = counts_2.get(num_b, 0) + 1
    
    return counts_1 == counts_2

    #solution, much cleaner - i believe using a helper function reduces the amount of dictionaries we have to define.
    #return freq_count(str(num1) == freq_counter(str(num2))
    

doctest.testmod(name='same_frequency', verbose=True)
