
# $ GENERATORS, ITERATORS, AND CLOSURES

# very simple snippet
for i in range(5): # - range is a generator (in fact, iterator)
  print(i)
# range is invoked six times, providing 5 subsequent values: 0, 1, 2, 3, 4 and finally signaling that the series is complete.


""" What is the difference ?
  A function returns one, well-defined value – it may be the result of a more or less complex evaluation of, something like a polynomial, and is invoked once – only once.

A generator returns a series of values, and in general, is (implicitly) invoked more than once.
"""


""" 
An iterator must provide two methods:

__iter__() which should return the object itself and which is invoked once (it's needed for Python to successfully start the iteration)

__next__() which is intended to return the next value (first, second, and so on) of the desired series – it will be invoked by the for/in statements in order to pass through the next iteration


If there are no more values to provide, the method should raise the StopIteration exception.
"""

# TODO: The first two Fibonacci numbers are equal to 1, any other Fibonacci number is the sum of the two preceding/previous ones. 1+1+2; 1+2=3; 2+3= 5 and so on...

# $ FIBONACCI ITERATOR OBJECT-ORIENTED VERSION

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i) 
""" 
Response obtained:

__init__
__iter__
__next__
1
__next__
1
__next__
2
__next__
3
__next__
5
__next__
8
__next__
13
__next__
21
__next__
34
__next__
55
__next__
"""

# | ****************************************************************************

class Fib2:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib2(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object:
    print(i)



# $ YIELD STATEMENT
# The yield statement is used to define a generator, replacing the return statement.
""" 
You may think of the yield keyword as a smarter sibling of the return statement, with one essential difference
"""

def fun(n):
    for i in range(n):
        #return i
        yield i # - yield is a generator. It returns a series of values, not just one.



# $ HOW TO BUILD A GENERATOR

def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v) # - 0 1 2 3 4


# TODO: What if you need a generator to produce the first n powers of 2 ?
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

# List comprehensions are not generators, but they can be used to create generators.
t = [x for x in powers_of_2(8)]
print(t) # - [1, 2, 4, 8, 16, 32, 64, 128]


# ? The list() function
# It can transform a series of subsequent generator invocations into a real list.
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = list(powers_of_2(3))
print(t) # - [1, 2, 4]


# ? The in operator
# Moreover, the context created by the in operator allows you to use a generator, too.

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for i in range(20):
    if i in powers_of_2(4): 
        print(i) # - 1 2 4 8 


# $ FIBONACCI GENERATOR SIMPLIFIED
""" 
Now let's see a Fibonacci number generator, and ensure that it looks much better than the object-oriented version based on the direct iterator protocol implementation
"""
def fibonacci(n):
    p = pp = 1 # p and pp are the first two Fibonacci numbers
    for i in range(n): # the generator will produce n Fibonacci numbers
        if i in [0, 1]: #  the first two numbers are equal to 1
            yield 1 #  the generator yields the first two numbers
        else:
            n = p + pp #  the next number is the sum of the two preceding ones
            pp, p = p, n #  the two preceding numbers are updated
            yield n # - the generator yields the next number

fibs = list(fibonacci(10)) # TODO: the generator is transformed into a list
print(fibs) # - [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# $ More about LIST comprehensions

list_1 = [] 

for ex in range(6): # ? Utilize a for loop
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)] # ? List comprehension builds the list in situ

print(list_1) # - [1, 10, 100, 1000, 10000, 100000]
print(list_2) # - [1, 10, 100, 1000, 10000, 100000]

# TODO: FORMULA -> [expression_one if condition else expression_two]

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list) # - [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

the_list = [1 if x % 2 == 0 else 0 for x in range(10)] # | expression_one if condition else expression_two

print(the_list) # - [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]


# $ List comprehension vs. generators
""" 
Now look at the code below and see if you can find the detail that turns a list comprehension into a generator.
"""

the_list = [1 if x % 2 == 0 else 0 for x in range(10)] # - Brackets are used to create a list comprehension
the_generator = (1 if x % 2 == 0 else 0 for x in range(10)) # - Parentheses are used to create a generator

for v in the_list:
    print(v, end=" ") # - 1 0 1 0 1 0 1 0 1 0
print()

for v in the_generator:
    print(v, end=" ") # - 1 0 1 0 1 0 1 0 1 0
print()

print(len(the_list)) # - 10
try:
  print(len(the_generator)) # - TypeError: object of type 'generator' has no len()
except TypeError as e:
  print(e)



# TODO: There is something elegant way to make the previous code since it is not necessary saving either the list or the generator in a variable. You can create them exactly in the place where you need them.


for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print() # - 1 0 1 0 1 0 1 0 1 0

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print() # - 1 0 1 0 1 0 1 0 1 0

""" 
!Note: the same appearance of the output doesn't mean that both loops work in the same way. In the first loop, the list is created (and iterated through) as a whole, it actually exists when the loop is being executed.

!In the second loop, there is no list at all, there are only subsequent values produced by the generator, one by one.
"""
