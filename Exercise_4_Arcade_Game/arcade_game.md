# Purpose

The purpose of this doc is to hold all the pseudocode for the [`arcade_game.py`](arcade_game.py) app. This file helps me to create a habit of thinking about the challenge before doing any coding.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Concepts

Concepts highlighted in the introduction:

- Python represents true and false values with the `bool` datatype
- Only two values in this datatype:
  - `True`
  - `False`
  - Each can be bound to a variable
- Evaluation of Boolean expressions are done using `and`, `or`, and `not` operators

## Pseudocode

Goal: pass all tests without errors

```Python
def eat_ghost(power_pellet_active, touching_ghost):
  # Pseudocode:
  # Test if power_pellet_active == True AND touching_ghost == True
    # If the statement above is true, return True
    # Else, return False

def score(touching_power_pellet, touching_dot):
  # Pseudocode:
  # Test if touching_power_pellet == True OR touching_dot == True
    # If the statement above is true, return True
    # Else, return false

def lose(power_pellet_active, touching_ghost):
  # Pseudocode:
  # Test if touching_ghost == True AND power_pellet_active == False
    # If the statement above is true, return True
    # Else, return false

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
  # Pseudocode:
  # Test if has_eaten_all_dots == True AND lose function returns False
    # If the statement above is true, return True
    # Else, return false
```
