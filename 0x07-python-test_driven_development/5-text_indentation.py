#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """
    Prints the given text with two newlines
    after each occurrence of '.', '?' or ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for i, char in enumerate(text):
        line += char
        if char in ".?:":
            print((line + '\n').lstrip())
            line = ""
    print(line.lstrip(), end='')

