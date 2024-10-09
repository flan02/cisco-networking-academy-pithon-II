
# ! In python online the first IMPORT occurs if you try to import the same module many times or embedded a module in another module it will only be imported once.
# TODO; Package -> Module -> Function

import sys

import module
print(__name__) # __main__

print("module counter", module.counter)

from module_advanced import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes)) # 0
print(prodl(ones)) # 1

import sys

# sys.path.append
# sys.path.insert

for p in sys.path:
  print(p)

from sys import path
path.append('..//packages')

import extra.iota
print(extra.iota.FunI())

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.good.best.tau import FunT


print(extra.good.best.sigma.FunS())
print(FunT())

print(alp.FunA())
print(sig.FunS())


""" 
 You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?
"""
if __name__ == "__main__":
    print("Do not do that!")
    sys.exit()