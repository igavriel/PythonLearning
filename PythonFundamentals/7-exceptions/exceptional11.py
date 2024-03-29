import sys

def convert(s):
    '''Convert a string to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {0}".format(str(e)))
        return -1
