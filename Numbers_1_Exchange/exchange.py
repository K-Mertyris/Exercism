"""
Currency Exhcnage exercise. Calculates various amounts of currency exchange based on inputs from the user.
"""

def estimate_value(budget, exchange_rate):
    """
    Estimates the value of your currency to the target currency
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - estimated value of the foreign currency you can receive
    """

    # Return the amount to exchange divided by the exchange rate
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """
    Calculates the amount of starting currency left after exchanging a specific amount
    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging
    """

    # Return the amount remaining after subtracting exchanging_value from budget
    return budget - exchanging_value

def get_value(denomination, number_of_bills):
    """
    Caculates the total value of bills in posession
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have
    """

    # Return total value of bills by multiplying denomination by number_of_bills
    return denomination * number_of_bills

def get_number_of_bills(budget, denomination):
    """
    Calculates the number of bills in posession after exchanging all money
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money
    """

    # Return the number of bills after exchanging using floor division (//)
    return budget // denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculates the maximum value of the exchanged currency based on starting currency, target currency, and exchange fees
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get
    """

    # Calculate total fees, change spread to a percentage
    fees = exchange_rate * (1 + (spread / 100))

    # Calculate value of budget after exchange and fees taken
    exchanged_value = budget / fees

    # Calculate number of bills that can be exchanged based on denomination
    number_of_bills = get_number_of_bills(exchanged_value, denomination)

    # Return value of exchange based on # of bills and denomination
    return get_value(denomination, number_of_bills)

def unexchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculates the unexchangeable value based on the starting currency, target currency and exchange fees
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - unexchangeable value
    """

    # TODO: Tech debt - refactor code to use exchangeable_value function

    # Calculate total fees, change spread to a percentage
    fees = exchange_rate * (1 + (spread / 100))

    # Calculate value of budget after exchange and fees taken
    exchanged_value = budget / fees

    # Calculate number of bills that can be exchanged based on denomination
    number_of_bills = get_number_of_bills(exchanged_value, denomination)

    # Calculate exchangeable value
    exchanging_value = get_value(denomination, number_of_bills)
    
    # Calculating leftover budget (change)
    remaining_budget = exchanged_value - exchanging_value

    # Cast remaining budget as int, round down, return value
    return int(remaining_budget)
