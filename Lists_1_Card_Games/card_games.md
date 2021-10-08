# Purpose

The purpose of this doc is to hold all the pseudocode for the [`meltdown.py`](meltdown.py) app. This file helps me to create a habit of thinking about the challenge before doing any coding.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Concepts

Concepts highlighted in the introduction:

### General

- `list` is a mutable (changeable) collection of items in sequence
  - `list`s can hold **references** to any or multiple data types, including other `list`s
  - Items in the list can be accessed via `0-based index` from the left and `-1-base index` from the right
  - Lists can be copied in whole or in part via **slice notation** or `<list>.copy()`
- Lists support common and mutable sequence operations
  - `min()`, `max()`
  - `<list>.index()`
  - `<list>.append()`
  - `<list>.reverse()`
- List items can be iterated over using
  - `for item in <list>`
- `for index, item in enumerate(<list>)`
  - Can be used when both the element index **and** the element value are needed
- `list`s are implemented as **dynamic arrays**

### Construction

- Declare lists: `<list> = []`, `<list> = [item1]`, `list = [item1, item2, itemn]`
  - Line breaks can be used when there are many elements or nested data structures within a list
- `list()` constructor can be used as an empty or iterable argument
  - `example_list_1 = list()`
  - `example_list_2 = list(("Parrot", "Bird", 334782))`
  - `example_list_3 = list({2, 3, 5, 7, 11})`
  - Printed:
    - example_list_1 = ""
    - example_list_2 = ['Parrot', 'Bird', 334782]
    - example_list_3 = [2, 3, 5, 7, 11]
- Using a `list` constructor with a string will have the list store individual letters of the string into the list
  - `example_list_string = list("Timbuktu")`
  - example_list_string = ['T', 'i', 'm', 'b', 'u', 'k', 't', 'u']
- Iteration default for **dictionaries** is over the **keys**, only key data will be inserted into the list
  - `example_list_dictionary = {"fish": "gold", "monkey": "brown"}`
  - example_list_dictionary = ['fish', 'monkey']
- `list` constructors will **only** take iterables or nothing as arguments
  - Objects that are not iterable will throw a `type` error
  - If you need to create a one-item `list`, use the literal method
    - Will not work: `element_list = list(16)`
    - Will work: `element_list = [16]` or `element_list = list((16,))`

### Accessing Elements

- Elements in lists can be accessed using bracket notation
  - `list[1]`, `list[0]`, `list[-1]`
- Sections of the elements in `list`s can be accessed via slice notation
  - `<list>[start:stop]`
    - NOTE: The `stop` index is not returned in the slice, the `start` is
  - Slice notation also allows for a `step` parameter where
    - `<list>[start:stop:step]`
    - `full_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]`
    - `skip_2_list = full_list[::2]`
    - skip_2_list = 0, 2, 4, 6, 8

### Iterating and Combining Lists

- Lists supply an iterator, can be iterated like sequence types

    ```python
    for item in <list>:
        print(item)

    for number in numbers_to_cube:
        print(number ** 3)
    ```

- Lists can also be combined using various techniques
  - `concatenate_list = ["Bob", 5] + ["dog", "Steve"]`
  - concatenate_list = ['Bob', 5, 'dog', 'Steve']
- Multiplying a list concatenates 'n' copies of the list
  - `original_list = ["cat", "dog", "elephant"]`
  - `multiplied_list = original_list * 3`
  - multiplied_list = ['cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant']`
- Appending through iteration
    ```python
    list_1 = ["cat", "Tabby"]
    list_2 = ["George", 5]

    for item in list_1:
        list_2.append(item)

    list_2
    ['George', 5, 'cat', 'Tabby']
    ```

## Pseudocode

Goal: pass all tests without errors

```Python
def get_rounds(number):
    # Pseudocode

def concatenate_rounds(rounds_1, rounds_2):
    # Pseudocode

def list_contains_round(rounds, number):
    # Pseudocode

def card_average(hand):
    # Pseudocode

def approx_average_is_average(hand):
    # Pseudocode

def average_even_is_average_odd(hand):
    # Pseudocode

def maybe_double_last(hand):
    # Pseudocode

```
