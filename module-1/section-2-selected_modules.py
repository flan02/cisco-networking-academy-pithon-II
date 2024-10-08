
# * LEARN MORE ABOUT PYTHON MODULES HERE
# - https://docs.python.org/3/py-modindex.html

import os
print(dir(os))
c=0
for name in dir(os):
    # print(name, end="\n")
    c += 1
    
print("Total of entities within the os module", c)

import math
print(dir(math)) # ? RECOMMENDABLE: It will return a list of the all entities of any object (say functions , modules, strings, lists, dictionaries etc.)

# ! You can access to complete list of entities using a for loop but it does not recommendable. 
c=0
for name in dir(math):
    # print(name, end="\n")
    c += 1
    
print("Total of entities within the math module", c)


from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

# ? The math module also provides functions for hyperbolic trigonometry
from math import sinh, cosh, tanh, asinh, acosh, atanh

# ? Exponentiation
from math import pow, e, exp, expm1, log, log1p, log2, log10, sqrt

print(pow(e,1) == exp(log(e))) # ? 2.718281828459045
print(pow(2,2) == exp(2 * log(2))) # ? 4.0
print(pow(e,e) == exp(0)) # ? 1.0

# ? The last group consists of some general-purpose functions like:
from math import ceil, floor, trunc, factorial, hypot, sqrt
x= 1.4
y= 2.6

print(floor(x), floor(y)) # ? 1 2
print(floor(-x), floor(-y)) # ? -2 -3
print(ceil(x), ceil(y)) # ? 2 3
print(ceil(-x), ceil(-y)) # ? -1 -2
print(trunc(x), trunc(y)) # ? 1 2
print(trunc(-x), trunc(-y)) # ? -1 -2

# $ RANDOM FUNCTION -> (Not to be confused with the module's name). It returns a float number
from random import random

print("Random Function")
for i in range(5):
    print(random())

# $ SEED FUNCTION -> It is used to initialize the random number generator
from random import seed
# seed() - sets tge seed with the current time
# seed(n) - sets the seed with an integer value
print("Seed Function")
seed(0) # ! Due to the seed value remains the same, the random function will always return the same value
for i in range(5):
    print(random())

# $ RANDRANGE & RADINT FUNCTION -> It returns a random integer chosen from the specified range
from random import randrange, randint
print("Randrange & Radint Function")
start=0
stop=1
step=1
print(randrange(1), end= " ") # ? 0
print(randrange(start, stop), end= " ") # ? 0
print(randrange(start, stop, step), end= " ") # ? 0
print(randint(start, stop)) # ? 0


for i in range(10):
    print(randint(1, 10), end=',') # ? 10,4,9,3,5,3,2,10,5,9

# $ CHOICE FUNCTION -> It returns a random element from the non-empty sequence
# $ SAMPLE FUNCTION -> It returns a list with a random selection of elements from the specified sequence

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list)) # ? 5
print(sample(my_list, 5)) # ? [3, 7, 2, 9, 10]
print(sample(my_list, 10)) # ? [10, 3, 6, 2, 5, 1, 9, 7, 4, 8]

# $ The PLATFORM function
# The platform module in Python is used to access the underlying platform’s data, such as hardware, operating system, and interpreter version information.
from platform import platform
platform(aliased = False, terse = False)
print("PLATFORM FUNCTION")
print(platform()) # ? Windows-10-10.0.19041-SP0
print(platform(1)) # ? Windows-10-10.0.19041-SP0
print(platform(0,1)) # ? Windows-10

# $ The MACHINE function
# Sometimes, you may need to know the machine type (processor) of the platform you are running on.
from platform import machine
print("MACHINE FUNCTION")
print(machine()) # ? AMD64

# $ The PROCESSOR function
# The processor() function returns the name of the processor for the current system.
from platform import processor
print("PROCESSOR FUNCTION")
print(processor()) # ? AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD

# $ The SYSTEM function
# The system() function returns the system/OS name.
from platform import system
print("SYSTEM FUNCTION")
print(system()) # ? Windows

# $ The VERSION function
# The version() function returns the system’s release version.
from platform import version
print("VERSION FUNCTION")
print(version()) # ? 10.0.19045


from platform import python_implementation, python_version_tuple

print(python_implementation()) # ? CPython

for atr in python_version_tuple(): # Python version
    # (x.x.x) -> major, minor, patch
    print(atr) # ? 3.12.6 
