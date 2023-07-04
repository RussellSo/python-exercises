
import doctest
def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    #a better hint would have been to say their is a sum() function
    # kind of interesting syntax - sum num in nums if its a float?

    return sum([num for num in nums if isinstance(num, float) ])

doctest.testmod(name='sum_floats', verbose=True)
