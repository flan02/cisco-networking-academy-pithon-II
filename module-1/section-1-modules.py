
# - PYTHON LIBRARIES FULL LIST (updated 2024)
# * https://docs.python.org/3/library/index.html

import math
import sys
# import math, sys


print(math.sin(math.pi/2))



def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

#from math import sin, pi
#print(sin(pi/2)) # ? 1.0


from math import * # * import all functions from math

# $ The as keyword -> is used to create an alias for a module
import math as m
print(m.sin(m.pi/2))

from math import sin as sine, pi as PI
print(sine(PI/2)) # ? 1.0