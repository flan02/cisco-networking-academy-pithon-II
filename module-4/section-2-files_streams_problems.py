
# $ Accesing files from Python code

""" 
One of the most common issues in the developer's job is to process data stored in files while the files are usually physically stored using storage devices – hard, optical, network, or solid-state disks
"""

# - File names
""" 
If you try to code it for the Windows system
 name = "\\dir\\file"
 name = "c:\\dir\\file"

This means that Windows file names must be written as follows:
name = "\\dir\\file"
"""


# - File streams
""" 
The opening of the stream is not only associated with the file, but should also declare the manner in which the stream will be processed. This declaration is called an open mode.

If the opening is successful, the program will be allowed to perform only the operations which are consistent with the declared open mode.


There are two basic operations performed on the stream:

read from the stream: the portions of the data are retrieved from the file and placed in a memory area managed by the program (e.g., a variable);
write to the stream: the portions of the data from the memory (e.g., a variable) are transferred to the file.


There are three basic modes used to open the stream:

read mode: a stream opened in this mode allows read operations only; trying to write to the stream will cause an exception (the exception is named UnsupportedOperation, which inherits OSError and ValueError, and comes from the io module);
write mode: a stream opened in this mode allows write operations only; attempting to read the stream will cause the exception mentioned above;
update mode: a stream opened in this mode allows both writes and reads.
"""

# TODO:  The stream behaves almost like a tape recorder.

""" 
When you read something from a stream, a virtual head moves over the stream according to the number of bytes transferred from the stream.

When you write something to the stream, the same head moves along the stream recording the data from the memory.

Whenever we talk about reading from and writing to the stream, try to imagine this analogy. The programming books refer to this mechanism as the current file position, and we'll also use this term.

It's necessary now to show you the object responsible for representing streams in programs.
"""


# $ Openning the streams

# TODO: stream = open(file, mode = 'r', encoding= None)

# ! If the opening is successfull, the function returns a stream object, otherwise it raises an exception. e.g. FileNotFoundError (If the file you're going to read doesn't exist).

""" 
the first parameter of the function (file) specifies the name of the file to be associated with the stream;

the second parameter (mode) specifies the open mode used for the stream; it's a string filled with a sequence of characters, and each of them has its own special meaning (more details soon);

the third parameter (encoding) specifies the encoding type (e.g., UTF-8 when working with text files)

the opening must be the very first operation performed on the stream.
"""
# Note: the mode and encoding arguments may be omitted – their default values are assumed then. The default opening mode is read in text mode, while the default encoding depends on the platform used.


# $ Let's see the most important and useful open modes
# TODO: Opening the streams: modes

# - r open mode: read
""" 
the stream will be opened in read mode;
the file associated with the stream must exist and has to be readable, otherwise the open() function raises an exception.
"""

# - w open mode: write
""" 
the stream will be opened in write mode;
the file associated with the stream doesn't need to exist; if it doesn't exist it will be created; if it exists, it will be truncated to the length of zero (erased); if the creation isn't possible (e.g., due to system permissions) the open() function raises an exception.
"""

# - a open mode: append
""" 
the stream will be opened in append mode;
the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; if it exists the virtual recording head will be set at the end of the file (the previous content of the file remains untouched).
"""

# - r+ open mode: read and update
""" 
the stream will be opened in read and update mode;
the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception;
both read and write operations are allowed for the stream
"""

# - w+ open mode: write and update
""" 
the stream will be opened in write and update mode;
the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; the previous content of the file remains untouched;
both read and write operations are allowed for the stream.
"""


# $ Selecting text and binary modes.
""" 
If there is a letter b at the end of the mode string, it means that the stream is to be opened in binary mode.

If the mode string ends with a letter t, the stream is opened in text mode.

Text mode is the default behaviour assumed when no binary/text mode specifier is used.

Finally, the successful opening of a file will set the current file position (the virtual reading/writing head) before the first byte of the file if the mode is not a and after the last byte of the file if the mode is set to a.
"""
""" 
| text mode | binary mode | description |
|-----------|-------------|-------------|
| r         | rb          | read        |
| w         | wb          | write       |
| a         | ab          | append      |
| r+        | r+b         | read/update |
| w+        | w+b         | write/update|
"""
# Extra: You can also open a file for its exclusive creation. You can do this using the x open mode. If the file already exists, the open() function will raise an exception.



# $ Opening the stream for the first time
# Imagine that we want to develop a program that reads the contents of the text file named:
# TODO: C:\Users\user\Desktop\file.txt

# ? How do we open that file for reading? Here's the relevant snippet of the code:

# file = "C:\\Users\\User\\Desktop\\file.txt"
file = r"C:\Users\User\Desktop\file.txt"  # TODO: Raw string (doesn't process the backslashes)
try:
    stream = open(file, "rt")
    # ! Processing goes here...
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)



# $ Pre-opened streams
""" 
We said earlier that any stream operation must be preceded by the open() function invocation. There are three well-defined exceptions to the rule.

When our program starts, the three streams are already opened and don't require any extra preparations. What's more, your program can use these streams explicitly if you take care to import the sys module:
"""
import sys

# TODO: The names of these streams are: 
# - sys.stdin, 
""" 
stdin (as standard input)
the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs;
the well-known input() function reads data from stdin by default.
"""

# - sys.stdout,
"""
stdout (as standard output)
the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program;
the well-known print() function outputs the data to the stdout stream.
"""

# - and sys.stderr.
""" 
tderr (as standard error output)
the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors encountered during its work;
we haven't presented any method to send the data to this stream (we will do it soon, we promise)
the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does not provide results) gives the possibility of redirecting these two types of information to the different targets. More extensive discussion of this issue is beyond the scope of our course. The operation system handbook will provide more information on these issues.
"""



# $ CLosing streams
""" 
The last operation performed on a stream (this doesn't include the stdin, stdout, and stderr streams, which don't require it) should be closing.

That action is performed by a method invoked from within the open stream object: stream.close().

the name of the function is definitely self-commenting: close()
the function expects exactly no arguments; the stream doesn't need to be opened
the function returns nothing, but raises an IOError exception in case of error;
most developers believe that the close() function always succeeds and thus there is no need to check if it's done its task properly.

This belief is only partly justified. If the stream was opened for writing and then a series of write operations were performed, it may happen that the data sent to the stream has not been transferred to the physical device yet (due to a mechanism called caching or buffering).

Since the closing of the stream forces the buffers to flush them, it may be that the flushes fail and therefore the close() fails too.
We have already mentioned failures caused by functions operating with streams, but we haven't said a word about how exactly we can identify the cause of the failure.

The possibility of making a diagnosis exists and is provided by one of streams' exception component which we are going to tell you about just now.
"""


# $ Diagnosing stream problems
""" 
The IOError object is equipped with a property named errno (the name comes from the phrase error number) and you can access it as follows
"""
try:
    # Some stream operations...
    stream = open("file.txt", "rt")
except IOError as exc:
    print(exc.errno)

# ! The value of the errno attribute can be compared with one of the predefined symbolic constants defined in the errno module.

# Let's take a look at some selected constants useful for detecting stream errors:
""" 
errno.EACCES → Permission denied

The error occurs when you try, for example, to open a file with the read only attribute for writing.

errno.EBADF → Bad file number

The error occurs when you try, for example, to operate with an unopened stream.

errno.EEXIST → File exists

The error occurs when you try, for example, to rename a file with its previous name.

errno.EFBIG → File too large

The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.

errno.EISDIR → Is a directory

The error occurs when you try to treat a directory name as the name of an ordinary file.

errno.EMFILE → Too many open files

The error occurs when you try to simultaneously open more streams than acceptable for your operating system.

errno.ENOENT → No such file or directory

The error occurs when you try to access a non-existent file/directory.

errno.ENOSPC → No space left on device

The error occurs when there is no free space on the media.
"""

# The complete list is much longer (it also includes some error codes not related to the stream processing).


""" 
TODO: If you are a very careful programmer, you may feel the need to use a sequence of statements similar to those presented in the editor.
"""

import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)

""" 
Fortunately, there is a function that can dramatically simplify the error handling code.

Its name is strerror(), and it comes from the os module and expects just one argument – an error number.

Its role is simple: you give an error number and get a string describing the meaning of the error.

Note: if you pass a non-existent error code (a number which is not bound to any actual error), the function will raise a ValueError exception.

Now we can simplify our code in the following wa
"""

from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))