
# $ Exceptions once again

# - We can add a block with the keyword finally to a try-except block. Additionally immediatly afther the try-except block we can add an else block that will be executed if the try block doesn't raise an exception.

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2)) # Everything went fine, It's time to say goodbye, 0.5
print(reciprocal(0)) # Division failed, It's time to say goodbye, None


# $ Exceptions are classes

try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())


def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)  # Tree of exceptions



# $ Anatomy of exceptions

def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')  
    print_args(e.args) 

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ') 
    print_args(e.args) 

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ') 
    print_args(e.args)


# $ Create your own exceptions

class MyZeroDivisionError(ZeroDivisionError):	# ? MyZeroDivisionError is a subclass of ZeroDivisionError
    pass


def do_the_division(mine): # ? mine is a boolean
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:		
        raise ZeroDivisionError("some bad news")


for mode in [False, True]: # ? mode is a boolean
    try:
        do_the_division(mode) 
    except ZeroDivisionError: # ? ZeroDivisionError is a class
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError: # ? MyZeroDivisionError is a subclass
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

""" 
Division by zero
Division by zero
Original division by zero
My division by zero
"""




class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)