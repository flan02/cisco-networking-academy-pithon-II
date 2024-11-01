
# $ OOP: Methods

""" 
Let's summarize all the facts regarding the use of methods in Python classes.

As you already know, a method is a function embedded inside a class.

There is one fundamental requirement – a method is obliged to have at least one parameter (there are no such things as parameterless methods – a method may be invoked without an argument, but not declared without parameters).

The first (or only) parameter is usually named self. We suggest that you follow the convention – it's commonly used, and you'll cause a few surprises by using other names for it.

The name self suggests the parameter's purpose – it identifies the object for which the method is invoked.

If you're going to invoke a method, you mustn't pass the argument for the self parameter – Python will set it for you.
"""

class Classy:
    def method(self):
        print("method")


obj = Classy() # create an object instance
obj.method() # invoke the method


class Classy2:
    def method(self, par):
        print("method:", par)


obj = Classy2()
obj.method(1) # invoke the method with an argument
obj.method(2) # invoke the method with another argument
obj.method(3) # invoke the method with yet another argument


class Classy3:
    varia = 2 # a class variable
    def method(self):
        print(self.varia, self.var) 


obj = Classy3()
obj.var = 3 # create an object variable on the fly
obj.method() # invoke the method its value is 2 (class variable) and 3 (on the fly object variable)


class Classy4:
    def other(self):
        print("other")

    def method(self):
        print("method") 
        self.other() 


obj = Classy4()
obj.method() # invoke the method its value will be method and other



class Classy5:
    def __init__(self, value):
        self.var = value


obj_1 = Classy5("object")

print(obj_1.var) # object

# ! THE CONSTRUCTOR CANNOT RETURN A VALUE... IT IS DESIGNED TO RETURN A NEWLY CREATED OBJECT AND NOTHING ELSE.
# ! CANNOT BE INVOKED DIRECTLY EITHER FORM THE OBJECT OR FROM INSIDE THE CLASS.



class Classy6:
    def __init__(self, value = None):
        self.var = value


obj_1 = Classy6("object")
obj_2 = Classy6()

print(obj_1.var) # object
print(obj_2.var) # None



class Classy7:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy7() 
obj.visible() # visible

try: # try to invoke __hidden if not it will print failed
    obj.__hidden() 
except:
    print("failed") # failed

obj._Classy7__hidden() # hidden


# TODO: The inner life of classes and objects

class Classy:
    pass


print(Classy.__name__) 
obj = Classy()
print(type(obj).__name__)
print(obj.__class__.__name__)

try:
    print(obj.__name__) # object has no attribute __name__
except AttributeError as e:
    print(e)
  
print(Classy.__module__)
obj = Classy()
print(obj.__module__)


""" 
__bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.

The order is the same as that used inside the class definition.

We'll show you only a very basic example, as we want to highlight how inheritance works.
"""

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne) # ( object )
printBases(SuperTwo) # ( object )
printBases(Sub) # ( SuperOne SuperTwo )


# TODO: Reflection and introspection

""" 
introspection, which is the ability of a program to examine the type or properties of an object at runtime;
reflection, which goes a step further, and is the ability of a program to manipulate the values, properties and/or functions of an object at runtime.
In other words, you don't have to know a complete class/object definition to manipulate the object, as the object and/or its class contain the metadata allowing you to recognize its features during program execution.
"""


# TODO: Investigating classes

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


# - Gets an object of any class, scans its contents in order to find all integer attributes with names starting with i, and increments them by one.
def incIntsI(obj):
    for name in obj.__dict__.keys(): # get all the keys of the object
        if name.startswith('i'): # check if the key starts with i
            val = getattr(obj, name) # get the value of the key
            if isinstance(val, int): # check if the value is an integer
                setattr(obj, name, val + 1) # set the value of the key to the value + 1


print(obj.__dict__) # ? {'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}
incIntsI(obj)
print(obj.__dict__) # ? {'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 5}










# TODO: Quizzes to test your understanding
""" 
Question 1: The declaration of the Snake class is given below. Enrich the class with a method named increment(), adding 1 to the victims property.
"""

class Snake:
    def __init__(self):
        self.victims = 0

    def increment(self):
        self.victims += 1


""" 
Question 2: Redefine the Snake class constructor so that is has a parameter to initialize the victims field with a value passed to the object during construction.
"""

class Snake:
    def __init__(self, victims):
        self.victims = victims


""" 
Question 3: Can you predict the output of the following code?
"""

class Snake:
    pass
 
 
class Python(Snake):
    pass
 
 
print(Python.__name__, 'is a', Snake.__name__) # Python is a Snake
print(Python.__bases__[0].__name__, 'can be', Python.__name__) # Snake can be Python




# TODO: LAB "The Timer Class"

""" 
We need a class able to count seconds. Easy? Not as easy as you may think, as we're going to have some specific requirements.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from the range [0..23] – we will be using military time), minutes (from the range [0..59]) and seconds (from the range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside the objects by +1/-1 second respectively.
Use the following hints:

all object properties should be private;
consider writing a separate function (not method!) to format the time string.
Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.
"""

print("LAB - The Timer Class")

def two_digits(val): # - function to format the time string
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer: # - Timer class
    def __init__(self, hours=0, minutes=0, seconds=0): # - constructor
        # ? private properties
        self.__hours = hours 
        self.__minutes = minutes 
        self.__seconds = seconds

    def __str__(self): # - printable
        # return the formatted time string
        return two_digits(self.__hours) + ":" + \
               two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)

    def next_second(self): # - next_second method
        # increment the time by 1 second
        self.__seconds += 1
        if self.__seconds > 59: # check if seconds is greater than 59
            self.__seconds = 0 # reset seconds to 0
            self.__minutes += 1
            if self.__minutes > 59: # check if minutes is greater than 59
                self.__minutes = 0 # reset minutes to 0
                self.__hours += 1
                if self.__hours > 23: # check if hours is greater than 23
                    self.__hours = 0 # reset hours to 0

    def prev_second(self): # - previous_second method
        # decrement the time by 1 second
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


timer = Timer(23, 59, 59) # create a Timer object
print(timer) # 23:59:59
timer.next_second() 
print(timer) # 00:00:00
timer.prev_second() 
print(timer) # 23:59:59



# TODO: "LAB - Days of the week"

""" 
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.

The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
all object's properties should be private;
"""


class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday) # Mon
    weekday.add_days(15)
    print(weekday) # Tue
    weekday.subtract_days(23)
    print(weekday) # Sun
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")



# TODO: " LAB - Points on a plane"

"""
Let's visit a very special place – a plane with the Cartesian coordinate system (you can learn more about this concept here: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Each point located on the plane can be described as a pair of coordinates customarily called x and y. We want you to write a Python class which stores both coordinates as float numbers. Moreover, we want the objects of this class to evaluate the distances between any of the two points situated on the plane.

The task is rather easy if you employ the function named hypot() (available through the math module) which evaluates the length of the hypotenuse of a right triangle (more details here: https://en.wikipedia.org/wiki/Hypotenuse) and here: https://docs.python.org/3.7/library/math.html#trigonometric-functions.

This is how we imagine the class:

it's called Point;
its constructor accepts two arguments (x and y respectively), both of which default to zero;
all the properties should be private;
the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);
the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;
the class provides a method called distance_from_point(point), which calculates the distance (like the previous method), but the other point's location is given as another Point class object;
"""

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        # - private properties
        self.__x = x
        self.__y = y

    def getx(self): # - gives access to the x coordinate
        return self.__x

    def gety(self): # - gives access to the y coordinate
        return self.__y

    def distance_from_xy(self, x, y): # - calculates the distance between the point stored inside the object and the other point given as a pair of floats
        return math.hypot(abs(self.__x - x), abs(self.__y - y)) # returns the distance between the two points

    def distance_from_point(self, point): # - calculates the distance between the point stored inside the object and the other point given as another Point class object
        return self.distance_from_xy(point.getx(), point.gety()) # returns the distance between the two points


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2)) # 1.4142135623730951
print(point2.distance_from_xy(2, 0)) # 1.4142135623730951


# TODO: LAB - Triangle
""" 
Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is what we want:

the constructor accepts three arguments – all of them are objects of the Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is the sum of all the lengths of the legs (we mention this for the record, although we are sure that you know it perfectly yourself.)
"""

import math


class Point: # - Point class
    # - constructor
    def __init__(self, x=0.0, y=0.0):
        # - private properties
        self.__x = x
        self.__y = y

    def getx(self): # - gives access to the x coordinate
        return self.__x

    def gety(self): # - gives access to the y coordinate
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle: # - Triangle class
    def __init__(self, vertice1, vertice2, vertice3):
        # - private properties
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        per = 0
        for i in range(3): # - loop through the vertices
            per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        return per


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1)) # create a Triangle object
print(triangle.perimeter()) # 3.414213562373095