# This random_array get a number and return a shuffle of the integers from 0 to the number

import sys
import random
from pprint import pprint as pp

class kv():
    def __init__(self, key, val):
        self._key = key
        self._val = val
        
    @property
    def key(self):
        return self._key
    
    @property
    def val(self):
        return self._val
    
    def __str__(self):
        return f"Item(key={self._key}, value={self._val})"


def random_array(num):
    arr = []
    # iterate from 1 to num
    # insert to array key=random, value=iter
    for i in range(0, int(num)):
        a_kv = kv(random.random(), i)
        arr.append(a_kv)

    #for item in arr:
    #    print(item)
        
    # sort array by keys 
    sorted_items = sorted(arr, key=lambda x: x.key)
    for item in sorted_items:
        print(item.val)


if __name__ == '__main__':
    if len(sys.argv)>1:
        random_array(sys.argv[1]) # The 0th arg is the module filename
    else:
        random_array(5)