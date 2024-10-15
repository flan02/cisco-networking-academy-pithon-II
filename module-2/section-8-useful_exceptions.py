
# TODO: Built-in exceptions
""" 
We're going to show you a short list of the most useful exceptions. While it may sound strange to call "useful" a thing or a phenomenon which is a visible sign of failure or setback, as you know, to err is human and if anything can go wrong, it will go wrong.
"""

# ! Exceptions are in fact objects – however, we can tell you nothing about this aspect until we present you with classes, objects, and the lik

# TODO: Know more about exceptions on your own in the following link
# ? https://docs.python.org/3/library/exceptions.html


# $ ArithmeticError
# Location: BaseException ← Exception ← ArithmeticError

# Description: an abstract exception including all exceptions caused by arithmetic operations like zero division or an argument's invalid domain



# $ AssertionError
# Location: BaseException ← Exception ← AssertionError

# Description: a concrete exception raised by the assert instruction when its argument evaluates to False, None, 0, or an empty string

from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))




# $ BaseException
#Location: BaseException

#Description: the most general (abstract) of all Python exceptions – all other exceptions are included in this one; it can be said that the following two except branches are equivalent: except: and except BaseException:.



# $ IndexError
#Location: BaseException ← Exception ← LookupError ← IndexError

#Description: a concrete exception raised when you try to access a non-existent sequence's element (e.g., a list's element)

# The code shows an extravagant way of leaving the loop.
the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True
 
while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False
 
print('Done')




# $ LookupError
#Location: BaseException ← Exception ← LookupError

# Description: an abstract exception including all exceptions caused by errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)



# $ MemoryError
#Location: BaseException ← Exception ← MemoryError

# Description: a concrete exception raised when an operation cannot be completed due to a lack of free memory.

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')



# $ OverflowError
#Location: BaseException ← Exception ← ArithmeticError ← OverflowError

#Description: a concrete exception raised when an operation produces a number too big to be successfully stored

from math import exp
 
ex = 1
 
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')




# $ImportError
#Location: BaseException ← Exception ← StandardError ← ImportError

#Description: a concrete exception raised when an import operation fails

try:
    import math
    import time
    #import abracadabra:  # ! this import doesn't exist
 
except:
    print('One of your imports has failed.')




# $ KeyError
#Location: BaseException ← Exception ← LookupError ← KeyError

#Description: a concrete exception raised when you try to access a non-existent element in a collection (e.g., a dictionary's element)

dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'
 
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)




# $ KeyboardInterrupt
#Location: BaseException ← KeyboardInterrupt

#Description: a concrete exception raised when the user uses a keyboard shortcut designed to terminate a program's execution (Ctrl-C in most OSs); if handling this exception doesn't lead to program termination, the program continues its execution.

#Note: this exception is not derived from the Exception class. Run the program in IDLE.

# This code cannot be terminated by pressing Ctrl-C.
#from time import sleep # ? this is needed to make the program sleep for one second

# seconds = 0

# while True:
#    try:
#        print(seconds)
#        seconds += 1
#        sleep(1)
#   except KeyboardInterrupt:
#        print("Don't do that!")




# TODO: LAB Reading ints safety
# This is how the function should react to the user's input:
""" 
Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)

Enter a number from -10 to 10: asd
Error: wrong input

Enter number from -10 to 10: 1
The number is: 1
"""


def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: wrong input")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
    return value;


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)


# $ SECTION SUMMARY

# ? Some abstract built-in Python exceptions are:
ArithmeticError,
BaseException,
LookupError


# ? Some concrete built-in Python exceptions are
AssertionError,
ImportError,
IndexError,
KeyboardInterrupt,
KeyError,
MemoryError,
OverflowError # This is a concrete exception raised when an operation produces a number too big to be successfully stored
