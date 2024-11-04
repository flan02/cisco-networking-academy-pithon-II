
# $ datetime module
# TODO: Common cases of use.
""" 
. event logging
. tracking changes in the database
. data validation
. storing important information
"""

# TODO: Getting the current local date and creating date objects
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)



my_date = date(2019, 11, 4) 
print(my_date) 



# TODO: Creating a date object from a timestamp
from datetime import date
import time

timestamp = time.time() # current timestamp
print("Timestamp:", timestamp) 

d = date.fromtimestamp(timestamp) # convert timestamp to date
print("Date:", d)



# TODO: Creating a date object using the ISO format
""" 
The datetime module provides several methods to create a date object. One of them is the fromisoformat method, which takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard.

The ISO 8601 standard defines how the date and time are represented. It's often used, so it's worth taking a moment to familiarize yourself with it. Take a look at the picture describing the values required by the format:
"""
# |  YYYY-MM-DD


# TODO: The replace() method
""" 
Sometimes you may need to replace the year, month, or day with a different value. You can’t do this with the year, month, and day attributes because they're read-only. In this case, you can use the method named replace.
"""

from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16) # ! replace year, month, day
print(d)


# TODO: What day of the week is it?
""" 
One of the more helpful methods that makes working with dates easier is the method called weekday. It returns the day of the week as an integer, where 0 is Monday and 6 is Sunday. Run the code in the editor
"""
from datetime import date

d = date(2024, 11, 3) 
print(d.weekday()) # 0 - Monday ... 6 - Sunday

print(d.isoweekday()) # 1 - Monday ... 7 - Sunday


# TODO: Creating time objects
""" 
You already know how to present a date using the date object. The datetime module also has a class that allows you to present time. Can you guess its name? Yes, it's called time:
"""

# | The time class constructor accepts the following optional parameters:
# . hour
# . minute
# . second
# . microsecond
# . tzinfo
# . fold
""" 
The tzinfo parameter is associated with time zones, while fold is associated with wall times. We won't use them during this course, but we encourage you to familiarize yourself with them.
"""

from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)



# TODO: The time module
""" 
In addition to the time class, the Python standard library offers a module called time, which provides a time-related function. You already had the opportunity to learn the function called time when discussing the date class. Now we'll look at another useful function available in this module.
"""
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds) # ! sleep for a given number of seconds
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5) # ? sleep for 5 seconds



# TODO: The ctime() function
""" 
The time module provides a function called ctime, which converts the time in seconds since January 1, 1970 (Unix epoch) to a string.
"""

import time

timestamp = 1572879180
print("timestamp converted to date: ", time.ctime(timestamp)) # ? convert timestamp to a string


import time
print(time.ctime()) # ? current date and time



# TODO: The gmtime() and localtime() functions
""" 
Some of the functions available in the time module require knowledge of the struct_time class, but before we get to know them, let's see what the class looks like:
"""

time.struct_time.tm_gmtoff # ? offset from UTC in seconds
time.struct_time.tm_hour # ? hour
time.struct_time.tm_isdst # ? daylight saving time flag
time.struct_time.tm_mday # ? day of the month
time.struct_time.tm_min # ? minute
time.struct_time.tm_mon # ? month
time.struct_time.tm_sec # ? second
time.struct_time.tm_wday # ? day of the week
time.struct_time.tm_yday # ? day of the year
time.struct_time.tm_year # ? year
time.struct_time.tm_zone

""" 
The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst.

The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes. Let's look at how to use the struct_time class in practice. Run the code in the editor.
"""

import time

timestamp = 1572879180
print(time.gmtime(timestamp)) # ? returns an object with the struct_time object in UTC
print(time.localtime(timestamp)) # ? returns a localtime object

# For the gmtime function, the tm_isdst attribute is always 0.



# TODO: The asctime() and mktime() functions
""" 
The time module has functions that expect a struct_time object or a tuple that stores values according to the indexes presented when discussing the struct_time class. Run the example in the editor.
"""
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st)) # ? converts a struct_time object or a tuple to a string
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))) # ? convert a tuple to a timestamp
    


# TODO: Creating datetime objects
""" 
In the datetime module, date and time can be represented either as separate objects or as one object. The class that combines date and time is called datetime.
"""
# datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)



# TODO: Methods that return the current date and time
""" 
The datetime class has several methods that return the current date and time. These methods are:

today() — returns the current local date and time with the tzinfo attribute set to None;
now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass;
utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.
"""
from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())
    


# TODO: Getting a timestamp
""" 
There are many converters available on the Internet that can calculate a timestamp based on a given date and time, but how can we do it in the datetime module?
This is possible thanks to the timestamp method provided by the datetime class. Look at the code in the editor.
"""
from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp()) # ? convert a datetime object to a timestamp



# TODO: Date and time formatting
""" 
All datetime module classes presented so far have a method called strftime. This is a very important method, because it allows us to return the date and time in the format we specify.

The strftime method takes only one argument in the form of a string specifying a format that can consist of directives.

A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter. For example, the directive %Y means the year with the century as a decimal number. Let's see it in an example. Run the code in the editor
"""
from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d')) # ? format the date as YYYY/MM/DD

# ! NOTE: You can find all available directives in the link below:
# | https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))




# TODO: The strftime() function in the time module
"""" 
You probably won't be surprised to learn that the strftime function is available in the time module. It differs slightly from the strftime methods in the classes provided by the datetime module because, in addition to the format argument, it can also take (optionally) a tuple or struct_time object.

If you don't pass a tuple or struct_time object, the formatting will be done using the current local time.
"""
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st)) # ? format the time using the struct_time object
print(time.strftime("%Y/%m/%d %H:%M:%S")) # ? format the current local time




# TODO: The strptime() methods
""" 
Knowing how to create a format can be helpful when using a method called strptime in the datetime class. Unlike the strftime method, it creates a datetime object from a string representing a date and time.

The strptime method requires you to specify the format in which you saved the date and time. Let's see it in an example.
"""
from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")) # ? create a datetime object from a string

# Its result will be as follows:
# - time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)



# TODO: Date and time operations
""" 
Sooner or later you'll have to perform some calculations on the date and time. Fortunately, there's a class called timedelta in the datetime module that was created for just such a purpose.

To create a timedelta object, just perform a subtraction on the date or datetime objects, just like we did in the example in the editor. Run it.

"""

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2) # ? calculate the difference between two date objects: 366 days, 0:00:00

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2) # ? calculate the difference between two datetime objects: 365 days, 9:07:00




# TODO: Creating timedelta objects
""" 
You've already learned that a timedelta object can be returned as a result of subtracting two date or datetime objects.

Of course, you can also create an object yourself. For this purpose, let's get acquainted with the arguments accepted by the class constructor, which are: days, seconds, microseconds, milliseconds, minutes, hours, and weeks. Each of them is optional and defaults to 0.
"""

from datetime import timedelta
 
delta = timedelta(weeks=2, days=2, hours=3) # ? create a timedelta object: 16 days, 3:00:00
print(delta)

""" 
The result of 16 days is obtained by converting the weeks argument to days (2 weeks = 14 days) and adding the days argument (2 days). This is normal behavior, because the timedelta object only stores days, seconds, and microseconds internally. Similarly, the hour argument is converted to minutes. Take a look at the example below:
"""

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3) # ? create a timedelta object: 16 days, 3:00:00
print("Days:", delta.days) # ? Days: 16
print("Seconds:", delta.seconds) # ? Seconds: 10800 -> 3 hours into seconds
print("Microseconds:", delta.microseconds) # ? Microseconds: 0


""" 
You already know how the timedelta object stores the passed arguments internally. Let's see how it can be used in practice.

Look at some operations supported by the datetime module classes. Run the code we've provided in the editor.
"""

from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta) # ? 16 days, 2:00:00

delta2 = delta * 2
print(delta2) # ? 32 days, 4:00:00

d = date(2019, 10, 4) + delta2
print(d) # ? 2019-11-05

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt) # ? 2019-11-05 18:53:00

""" 
The timedelta object can be multiplied by an integer. In our example, we multiply the object representing 16 days and 2 hours by 2. As a result, we receive a timedelta object representing 32 days and 4 hours.

Note that both days and hours have been multiplied by 2. Another interesting operation using the timedelta object is adding. In the example, we've added the timedelta object to the date and datetime objects.

As a result of these operations, we receive date and datetime objects increased by days and hours stored in the timedelta object.

The presented multiplication operation allows you to quickly increase the value of the timedelta object, while multiplication can also help you get a date from the future.

Of course, the timedelta, date, and datetime classes support many more operations. We encourage you to familiarize yourself with them in the documentation.
"""



# TODO: LAB - The datetime and time modules
""" 
Write a program that creates a datetime object for November 4, 2020 , 14:53:00. The object created should call the strftime method with the appropriate format to display the following result:

# ! Note: Each result line should be created by calling the strftime method with at least one directive in the format argument.
"""


from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53) # - create a datetime object; November 4, 2020, 14:53:00

print(my_date.strftime("%Y/%m/%d %H:%M:%S")) # - 2020/11/04 14:53:00 
print(my_date.strftime("%y/%B/%d %H:%M:%S %p")) # - 20/November/04 14:53:00 PM
print(my_date.strftime("%a, %Y %b %d")) # - Wed, 2020 Nov 04
print(my_date.strftime("%A, %Y %B %d")) # - Wednesday, 2020 November 04
print(my_date.strftime("Weekday: %w")) # - Weekday: 3
print(my_date.strftime("Day of the year: %j")) # - Day of the year: 309
print(my_date.strftime("Week number of the year: %W")) # - Week number of the year: 44



# TODO: Quiz
""" 
Question 1: What is the output of the following snippet?
"""

from datetime import time
 
t = time(14, 53)
print(t.strftime("%H:%M:%S")) # ? 14:53:00

""" 
Question 2: What is the output of the following snippet?
"""
 
dt1 = datetime(2020, 9, 29, 14, 41, 0)
dt2 = datetime(2020, 9, 28, 14, 41, 0)
 
print(dt1 - dt2) # ? 1 day, 0:00:00
