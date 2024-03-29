"""
This program parses sentences, and adds or removes suffixes from root words
Functions:
    add_prefix_un(word)
    make_word_groups(vocab_words)
    remove_suffix_ness(word)
    noun_to_verb(sentence, index)
"""

def add_prefix_un(word):
    """
    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    # Concatenate "un" to beginning of string, return string
    return "un" + word

def make_word_groups(vocab_words):
    """
    This function is expecting an array of words to be passed, not a sentence.
    
    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    
    # Store the prefix in a separate variable
    prefix = vocab_words[0]

    # Create word_groups string to return
    word_groups = prefix

    # Create separator to put between words in word_groups
    separator = " :: "

    # Iterate through elements in the array
    for index, word in enumerate (vocab_words):
        
        # Skip the prefix
        if index != 0:

            # Concatenate the separator and the prefix and current word to the existing string
            word_groups = word_groups + separator + prefix + word
    
    return word_groups

def remove_suffix_ness(word):
    """
    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    # TODO: There's got to be a better implementation of this than by hardcoding indexes

    # Read the string passed to the function and remove the last 4 characters
    root = word[:-4]

    # Read final character in the root word, if it is the 'i' character
    if root[-1] == "i":

        # Replace the 'i' with 'y'
        root = root[0:-1] + "y"

    # Return root word
    return root

def noun_to_verb(sentence, index):
    """
    This function is expecting a sentence and an index
        - The sentence can be any string of characters placed together and can end with a period, but no other punctuation
        - The index passed to the function is the index of the word to pull out of the sentence and change from a noun to a verb

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    # NOTE: Index passed is by word, not by letter
    
    # Store the suffix in a variable
    suffix = "en"

    # Split the sentence into a list of words that can be indexed
    noun = sentence.split()

    # Use the index passed to store the noun to convert to a verb
    verb = noun[index]

    # Test for period at end of string
    if verb[-1] == ".":

        # Remove the period by appending the suffix at index -1, return result
        return verb[:-1] + suffix

    # If no period at end of word, append suffix, return result
    return verb + suffix
