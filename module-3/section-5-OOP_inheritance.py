
# $ Inheritance

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sun", "Milky Way")
print(sun) # <__main__.Star object at 0x7f8b1c7b3b50>



class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self): # ? __str__ method is called whenever you use print() function
        return self.name + ' in ' + self.galaxy


sun = Star("Sun", "Milky Way")
print(sun)




# $ Example: Two-level inheritance

class Vehicle: # ? Superclass for both subclasses
    pass


class LandVehicle(Vehicle): # ? Subclass of Vehicle and Superclass of his son
    pass


class TrackedVehicle(LandVehicle): # ? Subclass for both classes
    pass




# $ issubclass() function
""" 
Python offers a function which is able to identify a relationship between two classes, and although its diagnosis isn't complex, it can check if a particular class is a subclass of any other class
"""

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]: # ? Loop through all classes
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]: # ? Loop through all classes
        print(issubclass(cls1, cls2), end="\t") # ? Check if cls1 is subclass of cls2
    print() 

""" 
|                 | Vehicle | LandVehicle | TrackedVehicle |
| Vehicle         | True    | False       | False          |
| LandVehicle     | True    | True        | False          |
| TrackedVehicle  | True    | True        | True           |
"""

# ! There is one important observation to make: each class is considered to be a subclass of itself. This is why the diagonal of the table is filled with True values.




# $ isinstance() function
""" 
The function returns True if the object is an instance of the class, or False otherwise.
Being an instance of a class means that the object (the cake) has been prepared using a recipe contained in either the class or one of its superclasses.
"""

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]: # ? Loop through all objects
    for cls in [Vehicle, LandVehicle, TrackedVehicle]: # ? Loop through all classes
        print(isinstance(obj, cls), end="\t") 
    print()

""" 
|                     | Vehicle | LandVehicle | TrackedVehicle |
| my_vehicle          | True    | False       | False          |
| my_land_vehicle     | True    | True        | False          |
| my_tracked_vehicle  | True    | True        | True           |
"""



# $ The is operator
print("The is operator")
""" 
The is operator checks whether two variables (object_one and object_two here) refer to the same object.
"""
# ! Don't forget that variables don't store the objects themselves, but only the handles pointing to the internal Python memory.


class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1 # | are actually the same object
object_3.val += 1

print(object_1 is object_2) # ? False
print(object_2 is object_3) # ? False
print(object_3 is object_1) # ? True
print(object_1.val, object_2.val, object_3.val) # ? 1 2 1

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

# | string_1 and string_2 aren't, despite their contents being the same.
print(string_1 == string_2, string_1 is string_2) # ? True False

# - Assigning a value of an object variable to another variable doesn't copy the object, but only its handle




# $ Example: Inheritance in practice
""" 
There is a class named Super, which defines its own constructor used to assign the object's property, named name.
the class defines the __str__() method, too, which makes the class able to present its identity in clear text form.
the class is next used as a base to create a subclass named Sub. The Sub class defines its own constructor, which invokes the one from the superclass. Note how we've done it: Super.__init__(self, name).
we've explicitly named the superclass, and pointed to the method to invoke __init__(), providing all needed arguments.
we've instantiated one object of class Sub and printed it.
"""

class Super:
    def __init__(self, name): # ? Constructor
        self.name = name

    def __str__(self): # ? __str__ method is called whenever you use print() function
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name): # ? Constructor
        # - Both ways are legit
        Super.__init__(self, name) # | Call the superclass constructor (inherited from Super)
        super().__init__(name) # | super() doesn't need to know the name of the superclass

obj = Sub("Andy")

print(obj) # ? My name is Andy.



# TODO: Testing properties: class variables.
class Super:
    superVar = 1

class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar) # ? 2
print(obj.superVar) # ? 1


# TODO: Testing properties: instance variables.
class Super:
    def __init__(self):
        self.superVar = 11 # | Create a new instance variable


class Sub(Super):
    def __init__(self): # ? subclass Constructor
        # - if you don't call (constructor) super().__init__() the superVar won't be created
        super().__init__() # | Call the superclass constructor
        self.subVar = 12   # | Create a new instance variable

obj = Sub() # ? Create an object of Sub class (instanciation)

print(obj.subVar) # ? 12
print(obj.superVar) # ? 11




# $ Summary inheritance
""" 
The example in the editor summarizes this in a three-level inheritance line. Analyze it carefully.
"""

class Level1:
    variable_1 = 100 # ? Class variable
    def __init__(self): # | Constructor
        self.var_1 = 101 # ? Instance variable

    def fun_1(self): # ? Method
        return 102 # - Return value


class Level2(Level1):
    variable_2 = 200 # ? Class variable
    def __init__(self): # | Constructor
        super().__init__() # ! Call the superclass constructor
        self.var_2 = 201 # ? Instance variable
    
    def fun_2(self): # ? Method
        return 202 # - Return value


class Level3(Level2): 
    variable_3 = 300 # ? Class variable
    def __init__(self): # | Constructor
        super().__init__() # ! Call the superclass constructor
        self.var_3 = 301 # ? Instance variable

    def fun_3(self): # ? Method
        return 302 # - Return value


obj = Level3() # ? Create an object of Level3 class (instanciation)

print(obj.variable_1, obj.var_1, obj.fun_1()) # | 100 101 102
print(obj.variable_2, obj.var_2, obj.fun_2()) # | 200 201 202
print(obj.variable_3, obj.var_3, obj.fun_3()) # | 300 301 302



# $ Multiple inheritance

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
 
 
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
 
 
class Sub(SuperA, SuperB): # | Inherit all the goods offered by both SuperA and SuperB
    pass
 
obj = Sub()
 
print(obj.var_a, obj.fun_a()) # ? 10 11
print(obj.var_b, obj.fun_b()) # ? 20 21



# $ Overriding
"""
What do you think will happen if more than one of the superclasses defines an entity of a particular name? 
"""

class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun()) # ? 200 201 -> The Level3 class object will be able to access only the entities defined in the Level2 class that means level1 class methods were overridden.

""" 
Both, Level1 and Level2 classes define a method named fun() and a property named var. Does this mean that the Level3 class object will be able to access two copies of each entity? Not at all.
"""



class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right): # | Pay attention to the order of the classes that are inherited
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun()) # ? L LL RR Left
# ! If I change the order of the classes that are inherited, the result will be different.
# - class Sub(Right, Left):  --->  R LL RR Right




# $ Hierarchy of classes

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One): # | Subclass of Class One.
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything() # ? do_it from One
two.doanything() # ? do_it from Two ---> Invoked just once (inside One class)

""" 
! Note: the situation in which the subclass is able to modify its superclass behavior (just like in the example) is called polymorphism.
! which means that one and the same class can take various forms depending on the redefinitions done by any of its subclasses.
"""

# TODO: Each class's behavior may be modified at any time by any of its subclasses

import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels()) 
tracked = Vehicle(Tracks())

# TODO: The turn() method is called for both objects, but the output is different.
# TODO: The ouput changes depending on the controller object passed to the Vehicle class
wheeled.turn(True) # ? wheels: True True
tracked.turn(False) # ? tracks: False True

# ! DON'T FORGET THAT

# ! multiple inheritance violates the single responsibility principle



# $ MRO (Method Resolution Order)
""" 
The MRO is the order in which Python looks for a method in a hierarchy of classes.
"""
class A:
    def speak(self):
        print("Soy A")

class B:
    def speak(self):
        print("Soy B")

class C(A, B):
    pass

obj = C()
obj.speak()  # Esto imprime "Soy A"

""" 
En este caso, el método speak de la clase A se llama primero, ya que A aparece antes que B en la definición de C(A, B). La MRO es [C, A, B, object]
"""

# TODO: Ask for the MRO either method are legit.
print(C.mro()) # ? [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(C.__mro__) # ? (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

"""
- Utilidad de MRO
El MRO garantiza que Python maneje correctamente la herencia múltiple, evitando ambigüedades y haciendo que el programa sea más predecible.
"""




# $ The Diamond Problem
"""
The diamond problem is an ambiguity that arises when two classes B and C inherit from A, and class D inherits from both B and C. If a method in D calls super().method(), which class method is invoked?
"""

# Take a look at the following code:
class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
	def m_bottom(self):
		print("bottom")


object = Bottom()

object.m_bottom() # ? bottom

object.m_middle() # ! middle_left **

object.m_top() # ? top

""" 
! **
In other words, what will you see on the screen: middle_left or middle_right?

You don't need to hurry – think twice and keep Python's MRO in mind!

Yes, you're right. The invocation will activate the m_middle() method, which comes from the Middle_Left class. The explanation is simple: the class is listed before Middle_Right on the Bottom class's inheritance list. If you want to make sure that there’s no doubt about it, try to swap these two classes on the list and check the results.
"""