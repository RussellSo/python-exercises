import doctest
def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    #case that end is defaulted to none so any function where end is not defined came back with a different result
    # so now that end is always defined as atleast the length, then we just have to add 1 to make the idx accurate
    if end is None:
        end = len(nums)
    return sum(nums[start:end + 1])
    # return sum(nums)
doctest.testmod(name='sum_range', verbose=True)
