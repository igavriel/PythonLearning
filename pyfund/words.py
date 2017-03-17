#!/usr/bin/env python3
"""Retrive and print words from a URL.

Usage:

    pythom words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL
    Args:
        url: the URL of a UTF-8 text document.

    Returns:
        A list of strings containg the words from the document.        
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)


def print_items(items):
    """Print items one per line.

    Args:
        An iteratable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from text documet form a URL

    Args:
        url: the URL of a UTF-8 text document.
    """
    if url == None:
        url = 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_items(words)


# technique to run from command line
if __name__ == '__main__':
    main(sys.argv[1])   # the '0' argument is the module file name
