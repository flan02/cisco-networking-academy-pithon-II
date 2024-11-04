
# $ The OS module interacting with the operating system

# TODO: Getting information about the operating system
import os 
print(os.name) # nt for windows, posix for linux

# TODO: Creating directories in Python

import os

try:
  os.mkdir("my_first_directory")
  print(os.listdir())
except FileExistsError:
  print("The directory already exists")


# TODO: Recursive directory creation
""" 
- NOTE: The equivalent of the makedirs function on Unix systems is the mkdir command with the -p flag, while in Windows, simply the mkdir command with the path:
"""

import os

try:
  os.makedirs("my_first_directory_recursive/my_second_directory_recursive")
  os.chdir("my_first_directory_recursive")
  print(os.listdir())
except FileExistsError:
  print("The directory already exists")


# $ Where am I now ?
""" 
As you’ve probably guessed, the os module provides a function that returns information about the current working directory. It's called getcwd.
"""
import os

try:
  os.makedirs("my_first_directory/my_second_directory")
  os.chdir("my_first_directory")
  print(os.getcwd())
  os.chdir("my_second_directory")
  print(os.getcwd())
except FileExistsError:
  print("The directory already exists")



# $ Deleting directories in PYthon
""" 
The os module also allows you to delete directories. It gives you the option of deleting a single directory or a directory with its subdirectories. To delete a single directory, you can use a function called rmdir, which takes the path as its argument. Look at the code in the editor.
"""
import os

os.mkdir("my_first_directory_removable") # create a directory
print(os.listdir())
os.rmdir("my_first_directory_removable") # delete a directory
print(os.listdir())

""" 
To remove a directory and its subdirectories, you can use the removedirs function, which requires you to specify a path containing all directories that should be removed:
"""

import os

os.makedirs("my_first_directory_removable/my_second_directory_removable")
os.removedirs("my_first_directory_removable/my_second_directory_removable")
print(os.listdir())



# $ The system() function
""" 
All functions presented in this part of the course can be replaced by a function called system, which executes a command passed to it as a string.

The system function is available in both Windows and Unix. Depending on the system, it returns a different result.

In Windows, it returns the value returned by the shell after running the command given, while in Unix, it returns the exit status of the process.

Let's look at the code in the editor and see how it is in practice.
"""

import os

returned_value = os.system("mkdir my_first_directory_with_system")
print(returned_value) # - 0 for success, 1 for failure