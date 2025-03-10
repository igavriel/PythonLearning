from ast import Assert
import sys
import random
from pprint import pprint as pp
from turtle import st

def string_stuff():
    print("string_stuff")
    str_example = 'ABC'
        
    assert(str_example[1]=='B')
    assert(str_example[1]=="B")
    assert(len(str_example)==3)
    assert(str_example.lower()=="abc")

    s1="-*" * 3
    assert(s1=="-*-*-*")
    
    # get user input
    #vegetable = input('Enter a name of a vegetable: ')
def math_stuff():
    print("math_stuff")
    power = 2 ** 10
    assert(power == 1024)   #power
    
def list_stuff():
    print("list_stuff")
    list_example = ['A', 'B', 'C']
    assert(list_example[1]=='B')
    
    list_example.append('D')
    assert(list_example[3]=='D')
    
    more_list = ['E', 'F']
    list_example.extend(more_list)
    assert(list_example[4]=='E')

def set_stuff():
    print("set_stuff")
    set_example = {'A', "B"}
    # direct access to set
    item = "A"
    if item in set_example:
        pass
    else:
        Assert(False)
    item = "C"
    if item not in set_example:
        pass
    else:
        Assert(False)

def dict_stuff():
    print("dict_stuff")
    dict_example = {'A': 1, "B":2}
    # direct access tp dict
    assert(dict_example["A"]==1)
    assert(dict_example['B']==2)
    # find value in dict
    assert(2 in dict_example.values())
    
def tuple_stuff():
    print("tuple_stuff")
    tuple_example = ('A', "B", "C")     # tuple is (), list is [], map and set is {}
    assert(tuple_example[1]=="B")
    
    list_from_tuple = list(tuple_example)
    assert(list_from_tuple[1]=='B')
    

    
if __name__ == '__main__':
#    if len(sys.argv)>1:
#        random_array(sys.argv[1]) # The 0th arg is the module filename
#    else:
#        random_array(5)
    string_stuff()
    math_stuff()
    list_stuff()
    set_stuff()
    dict_stuff()
    tuple_stuff()
    pass