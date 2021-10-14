"""
Card Games Exercise - the purpose of this app is to explore the use of lists and
functions that can manipulate lists
Functions:
    get_rounds(number)
    concatenate_rounds(rounds_1, rounds_2)
    list_contains_round(rounds, number)
    card_average(hand)
    approx_average_is_average(hand)
    average_even_is_average_odd(hand)
    maybe_double_last(hand)
"""

def get_rounds(number):
    """
    This function takes an incoming number, stores it in a list object, and
    appends the next two numbers in sequence to the list
    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    # Use the list constructor, start with empty list
    list_of_rounds = list()

    # Add items to the list, knowing we only want 3 total items in the list
    list_of_rounds.append(number)
    list_of_rounds.append(number + 1)
    list_of_rounds.append(number + 2)
    
    # Return list
    return list_of_rounds

def concatenate_rounds(rounds_1, rounds_2):
    """
    Concatenate two lists, with rounds_1 being first and rounds_2 being second
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    # No need for a constructor as we can do simple concatenation and return the
    # result
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """
    Search incoming list (rounds) for a specific number. Return True if match
    found, return False if no match found
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    # Iterate through list, searching for a match
    for round_number in rounds:
        # If match found, return True
        if round_number == number:
            return True

    # If no match found, return false
    return False


def card_average(hand):
    """
    Read incoming list and determine the average of the entire list
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    # Create variable to store the sum
    hand_sum = 0

    # Iterate through the list and add all elements
    for card in hand:
        hand_sum += card

    # Return average by dividing sum by the number of elements in the list
    return hand_sum / len(hand)


def approx_average_is_average(hand):
    """
    Compare shortcut ways of calculating average of hand dealt and return True
    if either shortcut is equal to the real average, false if neither is equal:
        Sum of first and last numbers in the hand
        Taking the median number of the hand
    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    # Store the two shortcut 'averages'
    first_last = (hand[0] + hand[-1])/2
    
    # Take the length of the list, subtract 1 and divide by 2 to ID the middle
    # index of the incoming list. This will only work here as all incoming lists
    # are known to be of odd length
    median = hand[int((len(hand)-1)/2)]

    # Determine the true average of the hand
    true_average = card_average(hand)

    # Compare the true average to the shortcut averages
    if true_average in (first_last, median):
        # If either average matches, return True
        return True

    # If neither average matches, return False
    return False


def average_even_is_average_odd(hand):
    """
    Split incoming list into even and odd elements of original list. Compare
    average of the even elements against the average of the odd elements.
    Demonstration of slice notation with lists
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    # Create variables, store sliced version of original list in respective
    # objects
    even_list = hand[::2]
    odd_list = hand[1::2]

    # Store averages in respective average variables
    even_average = card_average(even_list)
    odd_average = card_average(odd_list)

    # Test if even and odd averages are equal
    if even_average == odd_average:
        # If equal, return True
        return True

    # If not equal, return False
    return False


def maybe_double_last(hand):
    """
    Reads incoming list, if the last element is an '11', double it
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    # Test if last element of list is equal to 11
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2

    # Return the list, modified or not
    return hand
