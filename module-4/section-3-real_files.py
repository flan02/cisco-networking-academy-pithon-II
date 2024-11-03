
# $ Working with real files

# TODO: Processing text files.
from os import strerror

try: # Reading a file character by character
    counter = 0 # Counter for characters
    stream = open('file.txt', "rt") # Open file for reading text data
    char = stream.read(1) # Read the first character from the file
    while char != '': # While the last character is not an empty string
        print(char, end='') # Print the character
        counter += 1 # Increment the counter
        char = stream.read(1) # Read the next character from the file
    stream.close() # Close the file
    print("\n\nCharacters in file:", counter) # Print the number of characters in the file
except IOError as e: # Catch the exception
    print("I/O error occurred: ", strerror(e.errno)) # Print the error message


""" 
If you're absolutely sure that the file's length is safe and you can read the whole file to the memory at once, you can do it  the read() function, invoked without any arguments or with an argument that evaluates to None, will do the job for you.

! Remember: reading a terabyte-long file using this method may corrupt your OS.

Don't expect miracles... computer memory isn't stretchable.
"""

from os import strerror

try: # Reading a file character by character
    counter = 0 # Counter for characters
    stream = open('file.txt', "rt") # Open file for reading text data
    content = stream.read() # Read the whole file to the memory
    for char in content: # Iterate over the content
        print(char, end='') # Print the character
        counter += 1 # Increment the counter
    stream.close() # Close the file
    print("\n\nCharacters in file:", counter) # Print the number of characters in the file
except IOError as e: # Catch the exception
    print("I/O error occurred: ", strerror(e.errno)) # Print the error message


# $ readline() function
""" 
If you want to treat the file's contents as a set of lines, not a bunch of characters, the readline() method will help you with that.

The method tries to read a complete line of text from the file, and returns it as a string in the case of success. Otherwise, it returns an empty string.

This opens up new opportunities... now you can also count lines easily, not only characters.
"""

from os import strerror

try:
    character_counter = line_counter = 0 # Counters for characters and lines
    stream = open('file.txt', 'rt') # Open file for reading text data
    line = stream.readline() # Read the first line from the file
    while line != '': # While the last line is not an empty string
        line_counter += 1 # Increment the line counter
        for char in line: # Iterate over the line
            print(char, end='') # Print the character
            character_counter += 1 # Increment the character counter
        line = stream.readline() # Read the next line from the file
    stream.close() # Close the file
    print("\n\nCharacters in file:", character_counter) # Print the number of characters in the file
    print("Lines in file:     ", line_counter) # Print the number of lines in the file
except IOError as e: # Catch the exception
    print("I/O error occurred:", strerror(e.errno)) # Print the error message




# $ readlines() function
""" 
Another method, which treats text file as a set of lines, not characters, is readlines().

The readlines() method, when invoked without arguments, tries to read all the file contents, and returns a list of strings, one element per file line.

If you're not sure if the file size is small enough and don't want to test the OS, you can convince the readlines() method to read not more than a specified number of bytes at once (the returning value remains the same – it's a list of a string).
"""

stream = open("file.txt") # Open file for reading text data

# TODO: The maximum accepted input buffer size is passed to the method as its argument
print(stream.readlines(20)) # Read the first 20 bytes
print(stream.readlines(20)) # Read the next 20 bytes
print(stream.readlines(20)) # Read the next 20 bytes
print(stream.readlines(20)) # Read the next 20 bytes
stream.close() # Close the file


""" 
You may expect that readlines() can process a file's contents more effectively than readline(), as it may need to be invoked fewer times.

Note: when there is nothing to read from the file, the method returns an empty list. Use it to detect the end of the file.

To the extent of the buffer's size, you can expect that increasing it may improve input performance, but there is no golden rule for it – try to find the optimal values yourself.
"""
from os import strerror

try: # Reading a file line by line
    ccnt = lcnt = 0 # Counters for characters and lines
    s = open('text.txt', 'rt') # Open file for reading text data
    lines = s.readlines(20) # Read the first 20 bytes
    while len(lines) != 0: # While the last line is not an empty list
        for line in lines: # Iterate over the lines
            lcnt += 1 # Increment the line counter
            for ch in line: # Iterate over the line
                print(ch, end='') # Print the character
                ccnt += 1 # Increment the character counter
        lines = s.readlines(10) # Read the next 10 bytes
    s.close() # Close the file
    print("\n\nCharacters in file:", ccnt) # Print the number of characters in the file
    print("Lines in file:     ", lcnt) # Print the number of lines in the file
except IOError as e: # Catch the exception
    print("I/O error occurred:", strerror(e.errno)) # Print the error message


# $ Dealing with text files:
# TODO: write() function
""" 
The method is named write() and it expects just one argument – a string that will be transferred to an open file (don't forget – open mode should reflect the way in which the data is transferred – writing a file opened in read mode won't succeed).

No newline character is added to the write()'s argument, so you have to add it yourself if you want the file to be filled with a number of lines.

! Note: the open mode w ensures that the file will be created from scratch, even if it exists and contains data) and then puts ten lines into it.
"""

from os import strerror

try:
	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
     


try:
    file = open('newtext2.txt', 'wt')
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))



# $ What is a bytearray?
""" 
Before we start talking about binary files, we have to tell you about one of the specialized classes Python uses to store amorphous data.

Amorphous data is data which have no specific shape or form – they are just a series of bytes.

This doesn't mean that these bytes cannot have their own meaning, or cannot represent any useful object, such as bitmap graphics.

The most important aspect of this is that in the place where we have contact with the data, we are not able to, or simply don't want to, know anything about it.

Amorphous data cannot be stored using any of the previously presented means – they are neither strings nor lists.

There should be a special container able to handle such data.

Python has more than one such container – one of them is a specialized class name bytearray – as the name suggests, it's an array containing (amorphous) bytes.

If you want to have such a container, for example, in order to read in a bitmap image and process it in any way, you need to create it explicitly, using one of the available constructors.
"""
data = bytearray(10) # Create an array of bytes filled with 10 zeros

for i in range(len(data)): # Fill the array with some data
    data[i] = 10 - i # Fill the array with some data
    print(data[i]) # Print the data

for b in data: # Iterate over the data
    print(hex(b)) # | Print the data in hexadecimal form

""" 
! There is one important limitation – you mustn't set any byte array elements with a value which is not an integer (violating this rule will cause a TypeError exception) and you're not allowed to assign a value that doesn't come from the range 0 to 255 inclusive (unless you want to provoke a ValueError exception).
"""


from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.


# $ How to read bytes from a stream
""" 
Reading from a binary file requires the use of a specialized method name readinto(), as the method doesn't create a new byte array object, but fills a previously created one with the values taken from the binary file.

Note:
the method returns the number of successfully read bytes;
the method tries to fill the whole space available inside its argument; if there are more data in the file than space in the argument, the read operation will stop before the end of the file; otherwise, the method's result may indicate that the byte array has only been filled fragmentarily (the result will show you that, too, and the part of the array not being used by the newly read contents remains untouched)
"""
from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb') # Open the file for reading in binary mode
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


""" 
An alternative way of reading the contents of a binary file is offered by the method named read().

Invoked without arguments, it tries to read all the contents of the file into the memory, making them a part of a newly created object of the bytes class.

This class has some similarities to bytearray, with the exception of one significant difference, it's immutable.
"""

from os import strerror

try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read()) # Parameter indicate how many bytes must be read
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# ! Be careful – don't use this kind of read if you're not sure whether the file's contents will fit the available memory.



# $ Copying files - a simple and functional tool

""" 
Now you're going to amalgamate all this new knowledge, add some fresh elements to it, and use it to write a real code which is able to actually copy a file's contents.

Of course, the purpose is not to make a better replacement for commands like copy (MS Windows) or cp (Unix/Linux) but to see one possible way of creating a working tool, even if nobody wants to use it.
"""

from os import strerror

srcname = input("Enter the source file name: ") # Get the source file name
try: # Try to open the source file
    src = open(srcname, 'rb') 
except IOError as e: # Catch the exception
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ") # Get the destination file name
try: # Try to create the destination file
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536) # Create a buffer for copying
total  = 0 # Counter for copied bytes
try: # Copy the file
    readin = src.readinto(buffer)
    while readin > 0: # While there is something to read
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e: # Catch the exception
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written') # Print the number of copied bytes
src.close()
dst.close()



# TODO: LAB - Character frequency histogram
""" 
We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.
"""

from os import strerror

# Initialize 26 counters for each Latin letter.
# Note: we've used a comprehension to do that.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)} 

file_name = input("Enter the name of the file to analyze: ") # Get the file name
try:
    file = open(file_name, "rt") # Open the file for reading text data
    for line in file: # Iterate over the lines
        for char in line:  # Iterate over the characters
            # If it is a letter...
            if char.isalpha(): # If the character is a letter...
                # ... we'll treat it as lower-case and update the appropriate counter.
                counters[char.lower()] += 1 # Increment the counter
    file.close()
    # Let's output the counters.
    for char in counters.keys(): # Iterate over the counters
        c = counters[char] # Get the counter
        if c > 0: # If the counter is greater than 0
            print(char, '->', c)
except IOError as e: # Catch the exception
    print("I/O error occurred: ", strerror(e.errno))


# TODO: LAB - Sorted histogram
""" 
Let's make some improvements to our histogram. We want to sort the histogram by the frequency of the letters.
Use a lambda to change the sort order.
"""

from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close()
    file = open(file_name + '.hist', 'wt')
    # Note: we've used a lambda to access the directory's elements and set reverse to get a valid order.
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))



# TODO: LAB - Evaluating student's results
""" 
Your task is to write a program which:

asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:
"""

# A base exception class for our code:
class StudentsDataException(Exception):
    pass


# An exception for erroneous lines:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# An exception for an empty file.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

# A dictionary for students' data:
data = { }

file_name = input("Enter student's data filename: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Read the whole file into list.
    lines = f.readlines()
    f.close()
    # Is the file empty?
    if len(lines) == 0:
        raise FileEmpty()
    # Scan the file line by line.
    for i in range(len(lines)):
        # Get the i'th line.
        line = lines[i]
        # Divide it into columns.
        columns = line.split()
        # There shoule be 3 columns - are they there?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Build a key from student's given name and surname.
        student = columns[0] + ' ' + columns[1]
        # Get points.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Update dictionary.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Print results.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except WrongLine as e:
    print("Wrong line #" + str(e.line_number) + " in source file:" + e.line_string)
except FileEmpty:
    print("Source file empty")





# TODO: Highlighted quiz
""" 
Question 3: You're going to process a bitmap stored in a file named image.png, and you want to read its contents as a whole into a bytearray variable named image. Add a line to the following code to achieve this goal.
"""


try:
    stream = open("image.png", "rb")
    image = bytearray(stream.read()) # <--- Insert a line here.
    stream.close()
except IOError:
    print("failed")
else:
    print("success")