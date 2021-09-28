"""
    Return different states based on arguments passed to the application. All state testing done via boolean tests.
"""

def eat_ghost(power_pellet_active, touching_ghost):
    """
    This function determines whether Pac-man can eat a ghost or not
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    
    # Test if Pac-man is eating a ghost
    if power_pellet_active is True and touching_ghost is True:
        # If he is, return True
        return True
    
    # Otherwise return False
    return False


def score(touching_power_pellet, touching_dot):
    """
    This function determines whether Pac-man is earning points or not
    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    
    # Test if Pac-man is earning points
    if touching_power_pellet is True or touching_dot is True:
        # If he is, return True
        return True

    # Otherwise return False
    return False

def lose(power_pellet_active, touching_ghost):
    """
    This function determines whether Pac-man has lost or not
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    
    # Test if Pac-man lost
    if touching_ghost is True and power_pellet_active is False:
        # If he lost, return True
        return True

    # Otherwise return false
    return False

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    This function determines whether Pac-man has won the game or not
    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    
    # Test if Pac-man won the game
    if has_eaten_all_dots is True and lose(power_pellet_active, touching_ghost) is False:
        # If he won, return True
        return True

    # Otherwise return False
    return False
