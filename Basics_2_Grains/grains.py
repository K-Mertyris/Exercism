"""
This program calculates the number of grains on a chessboard given that the number of grains doubles with every square. Two numbers are calculated: 
    The number of grains on a particular square of a chessboard
    The number of total grains on a chessboard
Functions:
    square(number)
    total()
"""

def square(number):
    """
    This function calculates the number of grains on a particular square of a chessboard given that the number of grains doubles for every square
    :param number: Chessboard square number
    :return: Number of grains on the square
    """

    # Error checking: make sure incoming number is within the bounds of 1 - 64
    if number < 1 or number > 64:
        raise ValueError('Number out of bounds')

    # Multiply 2 to the power of the incoming number minus 1 (first square is 2^0, max square is 2^63), return result
    return 2 ** (number - 1)

def total():
    """
    This function calculates the number of total grains on the chessboard given that the number starts at 1 and doubles on every square. There are 64 squares on a chessboard
    :param: none
    :return: Number of total grains on the chessboard
    """

    # TODO: Loop back around to time this function. See if there's a more efficient way to calculate this sum

    # Create and initialize variables
    chessboard_squares = 64
    base_number = 2
    total = 0

    # Loop through all squares on the chessboard, sum result
    for i in range(chessboard_squares):
        total += base_number ** i

    return total
