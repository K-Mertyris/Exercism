# Purpose

The purpose of this doc is to hold all the pseudocode for the [`essay.py`](essay.py) app. This file helps me to create a habit of thinking about the challenge before doing any coding.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Concepts

Concepts highlighted in the introduction:

- Strings are **immutable sequences of Unicode code points**
- Stings can be iterated through using:
  - `for item in <str>`
  - `for index, item in enumerate(<str>)`
- Strings can be concatenated using:
  - The `+` operator
  - `<string>.join(<iterable>)
- **Immutability**: value of object in memory ***cannot*** change
  - Functions that operate on strings will return a new instance of the `str` object **instead of modifying** the original `str`
- Full list of string methods can be found in the [Python documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- `<str>.title()`: Capitalizes the first "character" of each "word" found
  - NOTE: output is dependent on the language codec used
- `<str>.endswith(<suffix>)`: Returns `True` if the string ends with `<suffix>` (whatever string of characters expected - **including punctuation**, returns `False` if suffix does not match
- `<str>.strip(<chars>)`: Returns a copy of the `str` with leading and trailing `<chars>` removed
  - **All combinations** of the chars will be removed from **both ends**
  - If no argument specified, removes whitespace
  - Multiple characters can be specified, no commas needed for list, just group the characters together
- `<str>.replace(<substring>, <replacement substring>)`: Returns a copy of the string with all occurrences of `<substring>` replaced with `<replacement substring>`
  - Don't use regex with this function, if regex is needed, import the `re` class
  - [More info on regex in Python](https://docs.python.org/3/howto/regex.html)

## Pseudocode

Goal: pass all tests without errors

```Python
def capitalize_title(title):
    # Pseudocode
    # Run incoming title variable through <str>.title() to capitalize the string
    # Return value

def check_sentence_ending(sentence):
    # Pseudocode
    # Test if the incoming sentence ends with a period (".")
    # Return result

def clean_up_spacing(sentence):
    # Pseudocode
    # Read incoming sentence
    # Test if first OR last characters are whitespace (" ")
    #   If yes, remove whitespace at the beginning and end of the sentence
    #   Return updated sentence
    # If no, return sentence as-is

def replace_word_choice(sentence, old_word, new_word):
    # Pseudocode
    # Read incoming values
    # Test if old_word exists in sentence
    #   If yes, replace old_word with new_word
    #   Return result
    # If no, return sentence


```
