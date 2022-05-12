"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""


def generate_phrase(characters, phrase):
    # accounted_for = ["t"]
    for char in phrase:
        if char in characters:
            characters.remove(char)
        else:
            return False
    return True


print(generate_phrase(["t", "t", "e", "s"], "test"))

## this is a different way to do it
import re


def generate_phrase(phrase):
    characters = re.compile(r'[^c-t-a]')
    phrase = characters.search(phrase)
    return not bool(phrase)


print(generate_phrase("act"))
