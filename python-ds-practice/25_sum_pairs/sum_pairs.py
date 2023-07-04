import doctest
def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    #goal - find first pair that adds to goal
    #had to look at solution - basically
    # this i would call a difference method which is
    # start with goal. Subtract first iterabale from goal - put into a new set
    # do again with next index - check is the difference in the set, because if it is then you have the two parts which should ultimately add up to the goal. 
    # what a crazy method.

    remaining_diff = set()

    for diff_check in nums:
        diff = goal - diff_check

        if diff in remaining_diff:
            return (diff, diff_check)
        
        remaining_diff.add(diff_check)
    return ()

doctest.testmod(name='sum_pairs', verbose=True)

