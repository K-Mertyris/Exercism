# Purpose

The purpose of this doc is to hold all the pseudocode for the [`grains.py`](grains.py) app. This file helps me to create a habit of thinking about the challenge before doing any coding.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Concepts

No concepts highlighted for this exercise. This is purely a math-based exercise. Will have to revisit the exercise when I learn about timing functions so I can optimize for time and readability.

## Pseudocode

Goal: pass all tests without errors

```Python
def square(number):
    # Pseudocode
    # Take incoming number and calculate how many grains are on that square of the chessboard
    # Formula: 2 ** number (2^number)
    #   The solution should be two to the power of whatever the incoming number is
    # Return solution

def total():
    # Pseudocode
    # Calculate the total number of grains on a chessboard if the number of grains doubles with each square
    #   There are 64 squares on a chessboard
    #   The first square has one grain (2^0)
    #   The 64th square has 2^63 grains on it (given that the first square is 2^0)
    #   I know there's an algebraic formula for this, I'll have to look it up
    # Return solution
```
