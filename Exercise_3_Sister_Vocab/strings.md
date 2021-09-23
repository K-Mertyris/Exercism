# Purpose

The purpose of this doc is to hold all the pseudocode for the `strings.py` app. This file helps me to create a habit of thinking about the challenge before doing any coding.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Pseudocode

Goal: pass all tests without errors

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

`def add_prefix_un(word):`  
`def make_word_groups(vocab_words):`  
`def remove_suffix_ness(word):`  
`def noun_to_verb(sentence, index):`
