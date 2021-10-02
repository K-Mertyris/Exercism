"""
This application runs through a series of checks for proper formatting in an essay.
Functions:
    def capitalize_title(title):
    def check_sentence_ending(sentence):
    def clean_up_spacing(sentence):
    def replace_word_choice(sentence, old_word, new_word):
"""

def capitalize_title(title):
    """

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """

    # Capitalize the incoming string as a title and return output
    return title.title()


def check_sentence_ending(sentence):
    """

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """

    # Check if the incoming string ends with a period, return true if it does, false if it doesn't
    return sentence.endswith(".")


def clean_up_spacing(sentence):
    """

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """

    # Strip incoming string of leading and trailing spaces, return updated string
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """

    :param sentence: str a sentence to replace words in.
    :param new_word: str replacement word
    :param old_word: str word to replace
    :return:  str input sentence with new words in place of old words
    """

    # Read incoming sentence, search for a word, replace with another word, return result
    return sentence.replace(old_word, new_word)
