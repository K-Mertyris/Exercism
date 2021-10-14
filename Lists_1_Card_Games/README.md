# Source

The instructions for this exercise can be found on the Exercism website. Please visit their website for more information. The group has done an AMAZING job at creating a resource to learn coding.

## Links

Resource links:

- [Exercism Website](https://exercism.org/)
- [Python Track](https://exercism.org/tracks/python)
- [Lists Concept](https://exercism.org/tracks/python/concepts/lists)
- [Exercise link](https://exercism.org/tracks/python/exercises/card-games)

## Requirements

### Requirements for this exercise

1. Check for criticality
2. Determine the Power output range
3. Create a Fail Safe Mechanism

## Current Status

Most recent updates shown first.

### 2021-10-13

- **Status**: In Progress
- **Notes**: Coding tonight. Added an extension [`Rewrap`](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap) to assist with making sure my Python code conforms to PEP-8 standards for line length. Will need to look into using `Black` and `Poetry` as I continue to work with Python.
- **Testing**: All tests passed, getting some recommendations from the Exercism linter about trailing whitespace and using `list[]` instead of `list()` in the `get_rounds` function. If I change the code, VS Code starts to throw an error, so not fixing that one for now. There was a good suggestion, I originally put:

```python
def approx_average_is_average(hand):
    """
    Compare shortcut ways of calculating average of hand dealt and return True
    if either shortcut is equal to the real average, false if neither is equal:
    """

    ...

    # Compare the true average to the shortcut averages
    if true_average == first_last or true_average == median:
        # If either average matches, return True
        return True

    # If neither average matches, return False
    return False
```

- With the recommendation, it got changed to:

```python
def approx_average_is_average(hand):
    """
    Compare shortcut ways of calculating average of hand dealt and return True
    if either shortcut is equal to the real average, false if neither is equal:
    """

    ...

    # Compare the true average to the shortcut averages
    if true_average in (first_last, median):
        # If either average matches, return True
        return True

    # If neither average matches, return False
    return False

```

### 2021-10-12

- **Status**: In Progress
- **Notes**: Writing out pseudocode. Not doing too much tonight as I need to get back to work. Will code more tomorrow.

### 2021-10-07

- **Status**: In Progress
- **Notes**: Setting up the folders and creating the basic files. Adding this exercise to the main [`README.md`](../README.md) in the root folder. Captured main concepts. Will come back tomorrow and write pseudocode and maybe code.
  - [`card_games.md`](card_games.md): Space to create pseudocode and capture other notes about the project
  - [`card_games.py`](card_games.py): Copied code from Exercism exercise
