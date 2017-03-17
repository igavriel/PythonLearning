PEP 8 - Python style guide
PEP 20 - The Zen of Python

## Loops
for i in range(5) :
	print(i)

four spaces as indentation

* import module
* from module import function
* from module import function as alias
* import filenamw without the py extension


import math

data types
* int  - sign
* float - 64 bit
* None - null
* bool
Relation
== != < > <= >=

int
0b10  == 2
0x10 == 16
int("42")

float 
3.125
3e8
1.616e-35
float(5)
float("nan")
float("inf")
float("-inf")

a = None
a is None --> True
bool("False") --> True cause strin is not empty

if expr:
	print("expr is True")
elif "SSS"
	print("expr is True")
else:
	print("expr is False")

while expr:
	print("loop")

c=5
while c!= 0:	// while c:
    print (c)
	c -= 1

Collections
str - unicode, immutable - 'sss' "ssss"  "ssss'ssss"
* "first" "second" --> 'firstsecond'
* \n  --> PEP278
* path = r'C:\Temp\' --> C:\Temp

bytes
d = b'some bytes'

list 
[1, 2, 3]
a = ["A", "AA", "AAA"]
a[1]  --> AA

dict
{k1:v1, k2:v2}
d={'ilan':'1111', 'bob':'2222'}


-----------------------------
__name__ 