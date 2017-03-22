Python Fundamentals
-------------------
https://app.pluralsight.com/player?course=python-fundamentals&author=austin-bingham&name=python-fundamentals-m06-exceptions&clip=0&mode=live

https://www.codecademy.com/articles/glossary-python


PEP 8 - Python style guide
PEP 20 - The Zen of Python

four spaces as indentation

import
```python
>>> import module
>>> from module import function
>>> from module import function as alias
>>> import filename without the py extension
```

example
> import math

Data types
----------
* **int**  - sign
* **float** - 64 bit
* **None** - null
* **bool** - True / False

Relation
--------
> == != < > <= >=

int
---
```python
0b10  == 2
0x10 == 16
int("42")
```

float 
-----
```python
3.125
3e8
1.616e-35
float(5)
float("nan")
float("inf")
float("-inf")
```

None
----
```python
a = None
a is None     #--> True
bool("False") #--> True cause string is not empty
```

Conditional
-----------
```python
if expr:
	print("expr is True")
elif "SSS"
	print("expr is True")
else:
	print("expr is False")
```

```python
while expr:
	print("loop")

c=5
while c!= 0:	// while c:
    print (c)
	c -= 1
```

Collections
-----------
**str** - unicode, immutable - 'sss' "ssss"  "ssss'ssss"
```python
>>> "first" "second" --> 'firstsecond'
>>> \n  --> PEP278
>>> path = r'C:\Temp\' --> C:\Temp
```

**list**
```python
[1, 2, 3]
a = ["A", "AA", "AAA"]
a[1]  #--> AA
```

**dict**
```python
{k1:v1, k2:v2}
d={'ilan':'1111', 'bob':'2222'}
```

------------------
module 5 - objects
------------------
**is** - equality of identity
**==** - test for equivalence
**import** and **def** - result in binding to named refernces
**type(xxx)** - determine the type of an object
**dir(xxx)** - interspect an objects and get its attributes
**__name__** - name of function or module object
**__doc__** - docstring of function or module object
**len()** - measure length of a string

Nested Scopes: Local, Enclosing, Global and Built-ins (LEGB)

----------------------
module 6 - collections
----------------------

tuple --> (x,c,b)
single tuple -- k=(11,)
empty tuple -- e()

**str** - unicode, immutable - 'sss' "ssss"  "ssss'ssss"
* \n  --> PEP278

| Command            | Result        |        
|--------------------|---------------|
| len("ssss")        | 4             |
| "SS" + "ss"        | "SSss"        |
| "first" "second"   | 'firstsecond' |
| path = r'C:\Temp\' | 'C:\Temp'     |

| Split/Join                      | Result          |        
|---------------------------------|-----------------|
| aa = ';'.join(['1', '2', '3'])  | '1;2;3'         |
| aa.split(';')                   | ['1', '2', '3'] |
| ''.join(['1', '2', '3'])        | '123'           |


* "Format {0} is {1} ({0})".format('aa', 123) --> format aa is 123 (aa)
* "var {}={}".format('aa',123) --> var aa=123

**range** - collection

|Constructor   |Argumetns       |Result         |        
|--------------|----------------|---------------|
|range(5)      | Stop           | 0,1,2,3,4     |
|range(5,10)   | Start,Stop     | 5,6,7,8,9     |
|range(10,20,2)| Start,Stop,Step| 10,12,14,16,18|

**list** - mutable sequence
```python
>>> s="split this string please".split()

>>> s
#  0        1        2          3
# -4       -3       -2         -1
['split', 'this', 'string ', 'please']

s[1] = 'this'	# zero based

s[-3] = 'this'	 # one based

part_s = s[1:-1] #['this', 'string']

new_s1 = s[:]		 # copy full slice list
new_s2 = s.copy()	 # copy method
new_s3 = list(s)	 # constructor

new_s1 is not s    # True
new_s2 is not s    # True
new_s3 is not s    # True
```

--------------------
module 7 - exception
--------------------
```python
def convert(s):
    '''Convert a string to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)))
        raise
```

------------------
module 8 - lambdas
------------------
```python
words = "The quick brown fox jumped over the lazy dog".split()
words
[len(word) for word in words]	# list of length of words
{len(word) for word in words}	# set of length of words

from pprint import pprint as pp
az_to_num = {'a':1, 'b':2, 'c':3}
pp(az_to_num)
num_to_az = {az: num for num, az in az_to_num.items()}
pp(num_to_az)

import os
import glob
file_sizes = { os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)
```