
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



# $ The lambda function
""" 
 Programmers use the lambda function to simplify the code, to make it clearer and easier to understand.
"""

#- A lambda function is a function without a name (you can also call it an anonymous function)

# TODO: --> lambda parameters: expression
two = lambda: 2 # ? always returns 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3): # What does these parameters do actually? # - 2 1 0 1 2
    print(sqr(a), end=" ") # - 4 1 0 1 4
    print(pwr(a, two())) # - 4 1 0 1 4



# $ How to use lambda functions and what for?

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly) # - f(-2)=18 f(-1)=8 f(0)=2 f(1)=0 f(2)=2

""" 
Can we avoid defining the poly() function, as we're not going to use it more than once? Yes, we can. This is the benefit a lambda can bring
"""

# ! Look at the example below. Can you see the difference?

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
 
# ? The code has become shorter, clearer, and more legible.
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2) # - f(-2)=18 f(-1)=8 f(0)=2 f(1)=0 f(2)=2



# $ Lambdas and the map() function

# In the simplest of all possible cases, the map() function:
# i.e. -> map(function, list) # ? takes two arguments, a function and a list.

""" 
The above description is extremely simplified, as:

the second map() argument may be any entity that can be iterated (e.g., a tuple, or just a generator).
map() can accept more than two arguments.
"""


# TODO: You can use the resulting iterator in a loop, or convert it into a list using list() function.

list_1 = [x for x in range(5)] # - [0, 1, 2, 3, 4]
list_2 = list(map(lambda x: 2 ** x, list_1)) # - [1, 2, 4, 8, 16] -> list form
print(list_2)  # - [1, 2, 4, 8, 16]

for x in map(lambda x: x * x, list_2): # - 1 4 16 64 256 -> powers of 2
    print(x, end=' ')
print() # - 1 4 16 64 256


# ! Try to imagine the same code without lambdas. Would it be any better? It's unlikely.



# $ Lambdas and the filter() function

""" 
Another Python function which can be significantly beautified by the application of a lambda is filter().

It expects the same kind of arguments as map(), but does something different, it filters its second argument while being guided by directions flowing from the function specified as the first argument (the function is invoked for each list element, just like in map()).

The elements which return True from the function pass the filter, the others are rejected.
"""

from random import seed, randint

seed() # - seed() function initializes the random number generator
data = [randint(-10,10) for x in range(5)] 
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data)) 

print(data) # - [-4, 6, -5, 4, 6]
print(filtered) # - [4, 6]



# $ A brief look at closures
""" 
Let's start with a definition: closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore. Intricate? A bit.
"""

def outer(par):
    loc = par
 
 
var = 1
outer(var)

try: # ! Any of these values can be accessed from the outside.
    print(par)
    print(loc)
except NameError as e:
    print(e)


# - Let's modified the code significantly
def outer(par):
    loc = par

    def inner(): 
        return loc
    return inner


var = 1
# | A closure has to be invoked in exactly the same way in which it has been declared.
fun = outer(var)
print(fun()) # - 1


""" 
Now look at the code in the editor. It is fully possible to declare a closure equipped with an arbitrary number of parameters, e.g., one, just like the power() function.
"""

def make_closure(par):
    loc = par 

    def power(p):
        return p ** loc 
    return power 


fsqr = make_closure(2) 
fcub = make_closure(3)

for i in range(5): # ? 0 1 2 3 4
    print(i, fsqr(i), fcub(i))  

""" ... response
0 0 0 
1 1 1 
2 4 8 
3 9 27 
4 16 64
"""    




# $ Section Summary

""" 
1. An iterator is an object of a class providing at least two methods (not counting the constructor):

__iter__() is invoked once when the iterator is created and returns the iterator's object itself;
__next__() is invoked to provide the next iteration's value and raises the StopIteration exception when the iteration comes to an end.


2. The yield statement can be used only inside functions. The yield statement suspends function execution and causes the function to return the yield's argument as a result. Such a function cannot be invoked in a regular way – its only purpose is to be used as a generator (i.e. in a context that requires a series of values, like a for loop).
"""


# - 3. A conditional expression is an expression built using the if-else operator. For example:
print(True if 0 >= 0 else False) # ? True


# - 4. A lambda function is a tool for creating anonymous functions. For example:
def foo(x, f):
    return f(x)

print(foo(9, lambda x: x ** 0.5)) # ? 3.0


# - 5. The map(fun, list) function creates a copy of a list argument, and applies the fun function to all of its elements, returning a generator that provides the new list content element by element. For example:

short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list) # ? ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor']


# - 6. The filter(fun, list) function creates a copy of those list elements, which cause the fun function to return True. The function's result is a generator providing the new list content element by element. For example:
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list) # ? ['Python', 'Monty']


# - 7. A closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore. For example:
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner


b_tag = tag('<b>')
print(b_tag('Monty Python')) # ? <b>Monty Python</b>




# $ Secion Quiz


""" Question 1: What is the expected output of the following code? """
class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # ! Yes, we know that y is not always considered a vowel.
        self.pos = 0 # The position of the next vowel to be returned.
 
    def __iter__(self): # ? The method returns the object itself.
        return self
 
    def __next__(self): # ? The method returns the next vowel.
        if self.pos == len(self.vow): # ? If there are no more vowels, the method raises the StopIteration exception.
            raise StopIteration 
        self.pos += 1 # ? The method increments the position of the next vowel.
        return self.vow[self.pos - 1] # ? The method returns the next vowel.
 
 
vowels = Vowels() 
for v in vowels: # ? The loop iterates through the vowels.
    print(v, end=' ') # | a e i o u y


""" 
Question 2: Write a lambda function, setting the least significant bit of its integer argument, and apply it to the map() function to produce the string 1 3 3 5 on the console
"""
# ! even: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# ! odd / uneven: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

any_list = [1, 2, 3, 4]
# Complete the line here.
even_list = list(map(lambda x: x | 1, any_list)) 
print(even_list) # ? [1, 3, 3, 5]


"""
Question 3: What is the expected output of the following code? 
"""
def replace_spaces(replacement='*'): 
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement 
 
 
stars = replace_spaces() # ? The function is invoked without arguments.
print(stars("And Now for Something Completely Different")) # | And*Now*for*Something*Completely*Different


# ! NOTE
# ? https://peps.python.org/pep-0008/#programming-recommendations

""" 
the Style Guide for Python Code, recommends that lambdas should not be assigned to variables, but rather they should be defined as functions.

This means that it is better to use a def statement, and avoid using an assignment statement that binds a lambda expression to an identifer. Analyze the code below:
"""

# - Recommended:
def f(x): return 3*x


# ! Not recommended:
f = lambda x: 3*x

