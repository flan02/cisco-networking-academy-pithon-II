
# $ INSTANCE VARIABLES
# These are variables that are unique to each instance of a class.

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass() # first = 1
example_object_2 = ExampleClass(2) # first = 2

example_object_2.set_second(3) # second = 3

example_object_3 = ExampleClass(4) # first = 4
# ? property added just on the fly
example_object_3.third = 5 # third = 5

print(example_object_1.__dict__) # {'first': 1}
print(example_object_2.__dict__) # {'first': 2, 'second': 3}
print(example_object_3.__dict__) # {'first': 4, 'third': 5}

""" 
Python objects, when created, are gifted with a small set of predefined properties and methods. Each object has got them, whether you want them or not. One of them is a variable named __dict__ (it's a dictionary).
"""


# $ Encapsulated Properties
print("Encapsulated Properties")

class ExampleClass2:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val):
        self.__second = val


example_object_1 = ExampleClass2() # first = 1
example_object_2 = ExampleClass2(2) # first = 2

example_object_2.set_second(3) # second = 3

example_object_3 = ExampleClass2(4) # first = 4
# ? property added just on the fly
example_object_3.third = 5 # third = 5

print(example_object_1.__dict__) # ? {'_ExampleClass2__first': 1}
print(example_object_2.__dict__) # ? {'_ExampleClass2__first': 2, '_ExampleClass2__second': 3}
print(example_object_3.__dict__) # - {'_ExampleClass2__first': 4, 'third': 5}

# ? Now, the first property is hidden from the outside world. It's still there, but it's not easily accessible.
print(example_object_1._ExampleClass2__first) # 1




# $ CLASS VARIABLES
print("CLASS VARIABLES")

class ExampleClass3:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass3.__counter += 1

example_object_1 = ExampleClass3()
example_object_2 = ExampleClass3(2)
example_object_3 = ExampleClass3(4)

# - We told you before that class variables exist even when no class instance (object) had been created.

print(example_object_1.__dict__, example_object_1._ExampleClass3__counter) # ?{'_ExampleClass3__first': 1} 3
print(example_object_2.__dict__, example_object_2._ExampleClass3__counter) # ?{'_ExampleClass3__first': 2} 3
print(example_object_3.__dict__, example_object_3._ExampleClass3__counter) # ?{'_ExampleClass3__first': 4} 3



# $ Introspection
print("Introspection")	
class ExampleClass4:
    varia = 1
    def __init__(self, val):
        ExampleClass4.varia = val


print(ExampleClass4.__dict__)
example_object4 = ExampleClass4(2)

# ! We can see the difference between these two __dict__ variables. The first one belongs to the class, and the second one belongs to the object.
print(ExampleClass4.__dict__)
print(example_object4.__dict__)



# $ Attribute's existence

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a) # 1

if hasattr(example_object, 'b'):
    print(example_object.b)

try:
    print(example_object.b) # ! AttributeError: 'ExampleClass' object has no attribute 'b'
except AttributeError as e:
    print(e) # or pass if you don't want to print the error


class ExampleClass6:
    attr = 1 # Class contains the attribute named attr but not prop


print(hasattr(ExampleClass6, 'attr')) # True
print(hasattr(ExampleClass6, 'prop')) # False


# $ One more example

class ExampleClass7:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass7()

print(hasattr(example_object, 'b')) # True
print(hasattr(example_object, 'a')) # True

print(hasattr(ExampleClass7, 'b')) # False
print(hasattr(ExampleClass7, 'a')) # True




# TODO: Quiz with useful exercises.
""" 
Which of the Python class properties are instance variables and which are class variables? Which of them are private?
"""

class Python:
    population = 1 # class variable
    victims = 0 # class variable
    def __init__(self):
        self.length_ft = 3 # instance variable
        self.__venomous = False # private instance variable


    
""" 
Question 2: You're going to negate the __venomous property of the version_2 object, ignoring the fact that the property is private. How will you do this?
"""

version_2 = Python() 
version_2._Python__venomous = not version_2._Python__venomous


""" 
Question 3: Write an expression which checks if the version_2 object contains an instance property named constrictor (yes, constrictor!).
"""

hasattr(version_2, 'constrictor') # False