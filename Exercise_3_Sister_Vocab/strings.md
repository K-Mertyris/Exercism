# Purpose

The purpose of this doc is to hold all the pseudocode for the `strings.py` app. This file helps me to create a habit of thinking about the challenge before doing any coding.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Concepts

Concepts highlighted in the introduction:

- Declaring string literals
- Declaring multi-line strings
- Concatenating strings
- Using `<str>.join(<iterable>)`
- Using 0-based indexes (arrays) and looping backwards using negative indexes
- No `char` datatype in Python, single characters are stored as a new `str` datatype with length of 1
- Selecting substrings using *slice notation* `<str>[<start>:stop:<step>]`
  - Results exclude the `stop` index
  - If no `start`, default index is 0
  - If no `stop`, default index is end of string
- Splitting strings using `<str>.split(<separator>)`
  - Where string is split whenever `separator` is found
  - Will return a **list** of substrings
  - List can also be indexed and split using `<str>.split()`
  - If no arguments (`separator`), default split is whitespace
  - Separators can be more than one character (ex: `,\n`)
- Since strings are arrays (my words), they can be iterated through
  - Individual code items: `for item in <str>`
  - Indexes with items: `for index, item in enumerate(<str>)`

## Pseudocode

Goal: pass all tests without errors

```Python
def add_prefix_un(word):
  # Pseudocode:
  # Take string and add "un"
  # Store new string and then return OR encapsulate code in return statement

def make_word_groups(vocab_words):
  # Pseudocode:
  # Read array
  # Split array into separate elements based on comma delimiter
  #   May need to remove a space if the space is part of the full string
  #   Pattern for input: [<prefix>, <word_1>, <word_2> ... <word_n>]
  # Iterate through separate elements
  #   concatenate prefix in front of words
  #   add each word to string to send back via return
  #   Pattern for output: <prefix> :: <str1> :: <str2>
  # Return string

def remove_suffix_ness(word):
  # Pseudocode:
  # Read string
  # Parse string into two parts <root> + "ness"
  # Take the root
  # If root ends in "i", replace with "y"
  # If root does not end in "i", do nothing
  # Return root

def noun_to_verb(sentence, index):
  # Pseudocode:
  # Read string (sentence)
  # Use incoming index to parse a single word from the string (sentence)
  #    Start at string[index] end at first instance of a space
  #    If no space, end at period
  #    If no space and no period, default to end of string
  # Take word as root, append "en" at end of word
  # Return word
```
