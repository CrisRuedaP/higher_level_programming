#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of characters: ., ? and :
"""


def text_indentation(text):
    """ prints a text

    Args:
        text(str): must be a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    jump = '\n'
    quote = '?' + jump
    dot = '.' + jump
    doubleDot = ':' + jump

    p = text.replace('?', quote)
    x = p.replace('.', dot)
    z = x.replace(':', doubleDot)

    splitted = z.split(jump)
    lenght = len(splitted)
    lastLine = splitted[lenght - 1]

    i = 0
    while i < lenght - 1:
        print(splitted[i].strip() + jump)
        i += 1
    print(lastLine.strip(), end="")
