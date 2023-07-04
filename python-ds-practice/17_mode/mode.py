import doctest
def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    #This problem felt unecessaraly difficult - how is there not an easier way to count items and returnt the max value?
    
    #creating a dict for pairs
    counts = {}

    # setting each num to a 0 counter default if nothing present OR adding +1
    # I see this a lot for counter functions
    for num in nums:
        counts[num] = counts.get(num, 0) + 1 # .get is to grab the value from the key
    
    # find highest the highest value in our counts function above
    #breaking down: max() a built in function like Math.max
    #dict.value() returns an object with just values
    max_value = max(counts.value())

    #basically we found the max value already. now using the k v pair destructuring we can refind the max v
    # and then just return that key within an if statement
    for (k,v) in counts:
        if v = max_value:
            return k


doctest.testmod(name='mode', verbose=True)
