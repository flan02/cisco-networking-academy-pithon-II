
from time import sleep
sleep(1)


import math
print(dir(math)) # 


# The compiled Python bytecode is stored in files which have their names ending with: .pyc

""" 
Assuming that the following three files: a.py, b.py, and c.py reside in the same directory, what will be the output produced after running the c.py file?

# file a.py
print("a", end='')

# file b.py
import a
print("b", end='')

# file c.py
print("c", end='')
import a
import b
"""

# The output will be: cab

print(__name__) # __main__



try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")



# for line in open('text.txt', 'rt'): # return an iterable object


""" 
try:
    #raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")
"""



var = 1
assert var != 0  # AssertionError: if var == 0



x = "\\\\"
print(len(x)) # 2


# x = "\\\"
print(len(x)) # Error



print(chr(ord('p') + 2)) # r



print(float("1.3")) # 1.3



class Class:
    def __init__(self, val=0):
        pass
# object = Class(1, 2) -> It's giving an error because the constructor of the Class class accepts only one argument. 



class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v


a = A()
b = a
b.set()
print(a.v) # 3




class A:
    A = 1
    def __init__(self):
        self.a = 0


print(hasattr(A, 'a')) # False




class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(A, C)) # False




import sys

sys.stderr # stderr is a file object used to display the error messages. Is normally associated with the console or terminal where the program was run.



class A:
    def __init__(self, v):
        self.__a = v + 1


a = A(0)
# print(a.__a) # AttributeError: 'A' object has no attribute '__a'




class A:
    def __init__(self):
        pass


# ! It's giving an error because the constructor of the A class doesn't accept any arguments.
# a = A(1)  
# print(hasattr(a, 'A'))





class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


class C(B, A):
    def c(self):
        self.a()


o = C()
o.c() # b



try:
    raise Exception(1, 2, 3)
except Exception as e:
     print(len(e.args))




def my_fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in my_fun(2):
    print(x, end='') # +++++++




class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end='') # abc




def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s()) # ***


# q = s.read(1) 


# for x in open('file', 'rt'): # rt: read text
#   print(x) 



numbers = [0, 2, 7, 9, 10]
# Insert line of code here.
foo = map(lambda num: num ** 2, numbers)
print(list(foo)) # [0, 4, 49, 81, 100]



numbers = [i*i for i in range(5)]
# Insert line of code here.
foo = list(filter(lambda x: x % 2, numbers))
print(foo) # [1, 9]




import random
#
# Insert lines of code here.
#
a = random.randint(0, 100)
b = random.randrange(10, 100, 3)
c = random.choice((0, 100, 3))
print(a,b,c) # 6,82,0
# ! Note: I dunno if the output is correct or not



import os

# os.mkdir('pictures')
# os.chdir('pictures')

print(os.getcwd()) # /home/runner/pictures
# ! Note: I dunno if the output is correct or not



import os
print(os.uname_result)



from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2) # 11:27:22




from datetime import timedelta

delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta * 2) # 28 days, 22:00:00




import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3)) # Sun Mon Tue Wed Thu Fri Sat

