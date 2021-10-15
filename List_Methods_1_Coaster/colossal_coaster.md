# Purpose

The purpose of this doc is to hold all the pseudocode for the [`colassal_coaster.py`](colossal_coaster.py) app. This file helps me to create a habit of thinking about the challenge before doing any coding.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Concepts

Concepts highlighted in the introduction:

### General

Same general information as found in [`card_games.md`](../Lists_1_Card_Games/card_games.md). Some additional information:

- When a `list` is manipulated with a `list-method`, the `list` object is ***altered***. If you do not want the ***original*** list changed, a `shallow copy` must be made using slice or `<list>.copy()`.

### Adding Items

- To add an item to the end of an **existing** `list`, use `<list>.append(<item>)`
- To add an item to a `list` at a specific index, use `<list>.insert(<index>, <item>)`
  - If the argument for `<index>` is greater than he final `index` on the `list`, the item will be added in the final position. Equivalent to using `<list>.append(<item>)`
- *More notes coming*

### Removing Items

- *Notes coming*

### Reversing and Reordering

- *Notes coming*

## Occurrences of an item in a list

- *Notes coming*

## Finding the index of items

- *Notes coming*

## Pseudocode

Goal: pass all tests without errors

```Python
def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    # Pseudocode

def find_my_friend(queue, friend_name):
    # Pseudocode

def add_me_with_my_friends(queue, index, person_name):
    # Pseudocode

def remove_the_mean_person(queue, person_name):
    # Pseudocode

def how_many_namefellows(queue, person_name):
    # Pseudocode

def remove_the_last_person(queue):
    # Pseudocode

def sorted_names(queue):
    # Pseudocode
```
