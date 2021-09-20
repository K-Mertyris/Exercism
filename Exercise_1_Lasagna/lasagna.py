"""
Baking lasagna exercise. Calculates multiple timers based on input from the user.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate how long it will take to prep lasagne based on layers added
    :param number_of_layers: int layers in lasagne
    :return: int time to prep lasagne derived from 'PREPARATION_TIME'

    Function that takes the acutal layers the lasagne needs as an argument
    and returns how many minutes it will take to prep based on the
    'PREPARATION_TIME'.
    """

    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate number of minutes spent cooking so far
    :param number_of_layers: int layers of lasagne
    :param elapsed_bake_time: int baking time already elapsed
    
    Function that takes the number of layers in the lasagne and time spent
    in the oven as an argument. Returns total cooking time so far.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
