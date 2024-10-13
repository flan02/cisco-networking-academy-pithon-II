
# TODO: Errors, failures, and other plagues.

import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of", x, "equals to", y)

""" 
Enter x: 3
The square root of 3.0 equals to 1.7320508075688772

Enter x: "2"
Traceback (most recent call last):
  File "main.py", line 3, in 
    x = float(input("Enter x: "))
! ValueError: could not convert string to float: '"2"'

Enter x: -2
Traceback (most recent call last):
  File "main.py", line 4, in 
    y = math.sqrt(x)
! ValueError: math domain error
"""

# $ Exceptions

value = 1
value /= 0

""" 
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    value /= 0
! ZeroDivisionError: division by zero
"""

my_list = []
x = my_list[0]

""" 
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    x = my_list[0]
! IndexError: list index out of range
"""

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if second_number != 0: # ! Avoid division by zero
    print(first_number / second_number)
else:
    print("This operation cannot be done.")

print("THE END.")


# ! TRY - EXCEPT

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")


try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("THE END.")


try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")