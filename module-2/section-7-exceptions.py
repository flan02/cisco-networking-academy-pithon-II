
# $ EXCEPTIONS

# - Look at small section of the complete exceptions tree image in public folder py_exceptions.png

""" 
The exception is the same, but the more general exception is now listed first. It will catch all zero divisions too. It also means that there's no chance that any exception hits the ZeroDivisionError branch. This branch is now completely unreachable.
"""

try:
    y = 1 / 0
except ZeroDivisionError: # has priority
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")


try:
    y = 1 / 0
except ArithmeticError: # has priority
    print("Arithmetic problem!") 
except ZeroDivisionError:
    print("Zero Division!")
 
print("THE END.")


# TODO: If you want to handle two or more exceptions in the same way, you can use the following syntax:

# $ RAISE
""" 
. simulate raising actual exceptions (e.g., to test your handling strategy)
. partially handle an exception and make another part of the code responsible for completing the handling (separation of concerns)
"""

def bad_fun(n):
    raise ZeroDivisionError # raise keyword to raise an exception


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")


def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise # keyword to re-raise the exception


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")


# $ ASSERT
"""
. it evaluates the expression;
. if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value different than None, it won't do anything else;
. otherwise, it automatically and immediately raises an exception named AssertionError (in this case, we say that the assertion has failed) 
""" 

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x) # if x is negative, the program will raise an AssertionError exception




def foo(x):
    assert x 
    return 1/x
 
 
try:
    print(foo(0))
except ZeroDivisionError:
    print("zero") 
except:
    print("some") # AssertionError: if x is False, the program will raise an AssertionError exception


""" 
! RAISE 
se usa para lanzar excepciones manualmente cuando detectas un error en el programa.

! ASSERT 
se usa para verificar suposiciones o condiciones lógicas importantes durante el desarrollo, y lanza automáticamente una excepción cuando esas suposiciones fallan.
"""