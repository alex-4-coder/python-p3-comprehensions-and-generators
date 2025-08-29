#!/usr/bin/env python3

def return_evens(sequence):
    """
    Return a list of all even elements from the input sequence using a list comprehension.
    Example:
    return_evens([0, 1, 3, 5, 7, 8, 9]) -> [0, 8]
    """
    return [n for n in sequence if n % 2 == 0]


def make_exclamation(sentences):
    """
    Return a list of sentences with exclamation marks added using a list comprehension.
    Example:
    make_exclamation(["Hello", "I'm doing great", "Python is fun"])
    -> ["Hello!", "I'm doing great!", "Python is fun!"]
    """
    return [sentence + "!" for sentence in sentences]
