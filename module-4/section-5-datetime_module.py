
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