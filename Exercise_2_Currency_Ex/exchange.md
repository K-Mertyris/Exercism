# Purpose

The purpose of this doc is to hold all the pseudocode for the `exchange.py` app. Future apps built using the exercism site will have a file similar to this one to help me create good habits of documentation and thinking about the problem before solutioning.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Pseudocode

```Python
def estimate_value(budget, exchange_rate):
def get_change(budget, exchanging_value):
def get_value(denomination, number_of_bills):
def get_number_of_bills(budget, denomination):
```

No pseudocode written for these functions, please see the [README.md](/Exercise_2_Currency_Ex/README.md) for abbreviated instructions or the [code](exchange.py) for function details.

`def exchangeable_value(budget, exchange_rate, spread, denomination):`

```Python
    # Pseudocode
    # Calculate the max value based on budget, exchange_rate, spread & denomination
    # Calculate fees -> exchange rate + percentage taken as fee (exchange rate * spread as a percentage) Note that spread comes in as an int
    # Calculate how much can be exchanged based on fees (rate + fee) -> budget / fees
    # Calculate how MANY bills of a denomination will be received based on exchanged value using floor division -> exchanged value // denomination
    # Calculate max value of exchanged currency -> bills received * denomination
    # Return max value
```

`def unexchangeable_value(budget, exchange_rate, spread, denomination):`

```Python
    # Pseudocode
    # Calculate value remaining after currency exchanged
    # Calculate fees -> exchange rate + percentage taken as fee (exchange rate * spread as a percentage) Note that spread comes in as an int
    # Calculate how much can be exchanged based on fees (rate + fee) -> budget / fees
    # Calculate how MANY bills of a denomination will be received based on exhcnaged value using floor division -> exchanged value // denomination
    # Calculate how much can be exchanged -> number of bills * denomination
    # Calculate left over value of budget -> budget - total exchanged
    # Cast remaining value as int, rounding down
    # Return remaining value
```
