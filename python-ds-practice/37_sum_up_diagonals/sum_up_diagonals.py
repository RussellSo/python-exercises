import doctest
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    #set a total to keep track
    total = 0

    for i in range(len(matrix)): # seperates lists? range(2): i = 1 and then 2? # crazy but this is another way of looping for i.
        total += matrix[i][i] # i think this is just adding everything together
        total += matrix[i][-1 - i] # this is something that grabs diagonals?
        
    return total
doctest.testmod(name='sum_up_diagonals', verbose=True)
