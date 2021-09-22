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

    # Pseudocode
    # Calculate the max value based on budget, exchange_rate, spread & denomination
    # Calculate fees -> exchange rate + percentage taken as fee (exchange rate * spread as a percentage) Note that spread comes in as an int
    # Calculate how much can be exchanged based on fees (rate + fee) -> budget / fees
    # Calculate how MANY bills of a denomination will be received based on exchanged value using floor division -> exchanged value // denomination
    # Calculate max value of exchanged currency -> bills received * denomination
    # Return max value

    # Return max value of exchanged currency by dividing the budget by the exchange rate + the spread (as a percentage), 
    # then using floor division to determine how many bills can be exchanged
    return get_number_of_bills((budget/(exchange_rate + (exchange_rate/spread))), denomination) * denomination

def unexchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculates the unexchangeable value based on the starting currency, target currency and exchange fees
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - unexchangeable value
    """

    # Not going to touch this function right now, see if it passes its checks once exchangeable_value is updated and passes tests

    # Determine total fee rate
    calculated_exchange_fees = exchange_rate + (exchange_rate / spread)

    # Determine total amount to exchange less fees
    total_to_exchange = estimate_value(budget, calculated_exchange_fees)

    # Determine how much can be exchanged based on bill denomination
    can_exchange = get_number_of_bills(total_to_exchange, denomination)

    leftover_amount = get_change(total_to_exchange, (can_exchange * denomination))

    return leftover_amount
