
# TODO: Procedural approach to Object Oriented Approach

# STACK -> LIFO (Last In First Out)
# It is an object that has two operations: push (put a new element on the top) and pop (take out the last element)

# We can create and Stack either using a procedural approach or an object-oriented approach

# $ Procedural Approach
stack = [] # how to store the values

# define a fc that puts a value onto the stack
def push(val):
    stack.append(val)

# define a fc that takes a value off the stack
def pop(): # doesn't check if there is any elem in the stack
    val = stack[-1]
    del stack[-1]
    return val

push(3) # 1 elem in the stack
push(2) # 2 elem in the stack
push(1) # 3 elem in the stack

print(pop())
print(pop())
print(pop())


# ! The procedural approach is not the best way to implement a stack
# TODO Due to the fact that the stack is a data structure that has a state and behavior, it is better to implement it using an object-oriented approach since it is more natural to represent the state and behavior of the stack.

# $ Object-Oriented Approach
class Stack:
    def __init__(self): # ? constructor name is __init__ always
        print("Hi! I am a stack")
        self.stack_list = [] # stack_list is an attribute of the class Stack
        self.__stack_list = [] # - __stack_list is a private attribute of the class Stack

stack_object = Stack() # create an object of the class Stack (Instanciation)
print(len(stack_object.stack_list)) # 0
# print(len(stack_object.__stack_list)) # ! Inaccessible 


# $ Implement push n pop operation using object-oriented approach
print("Implement PUSH and POP operation using object-oriented approach")

# TODO: Our original stack class
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
print("First instance")
stack_object = Stack()

stack_object.push(3) # 1 elem in the stack
stack_object.push(2) # 2 elem in the stack
stack_object.push(1) # 3 elem in the stack

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

print("Second instance")
stack_object_2 = Stack()

stack_object.push(3)
stack_object_2.push(stack_object.pop())

print(stack_object_2.pop()) # 3

little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print(funny_stack.pop()) # 0



# TODO: Let's add a new class for handling stacks

class AddingStack(Stack):
    #pass
    def __init__(self):
        Stack.__init__(self) # call the constructor of the parent class
        self.__sum = 0

    def get_sum(self):
        return self.__sum
    
    # $ Override the push method of the parent class

    def push(self, val):
        self.__sum += val
        Stack.push(self, val) # call the push method of the parent class
    
    def pop(self):
        val = Stack.pop(self) # call the pop method of the parent class
        self.__sum -= val
        return val # return the value that was popped

stack_object = AddingStack()

for i in range(5):
    stack_object.push(i) # 0, 1, 2, 3, 4
print(stack_object.get_sum()) # 10  

for i in range(5):
    print(stack_object.pop())



# TODO LAB: Queue aka LIFO (Last In First Out)
print("LAB: Queue aka LIFO (Last In First Out)")
""" 
Your task is to implement the Queue class with two basic operations:

put(element), which puts an element at end of the queue;
get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)

Follow the hints:

use a list as your storage (just like we did with the stack)
put() should append elements to the beginning of the list, while get() should remove the elements from the end of the list;
define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to operate on an empty list.
"""

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError  # raise an exception if the queue is empty
        
que = Queue()
que.put(1)
que.put("Dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")


# TODO LAB: Queue aka FIFO (First In First Out)
print("LAB: Queue aka FIFO (First In First Out)")
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        return len(self.queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")