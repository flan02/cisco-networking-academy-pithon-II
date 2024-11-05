
# $ Calendar module

# TODO: Your first calendar

import calendar

print(calendar.SUNDAY) # 6

"""
calendar -> Parameters
w: date column width (default 2)
l: number of lines per week (default 1)
c: number of spaces between month columns (default 6)
m: number of columns (default 3)
"""
print(calendar.calendar(2020, w = 4)) # prints the calendar of 2020

import calendar
calendar.prcal(2024) # prints the calendar of 2024



# $ Calendar for a specific month
""" 
The calendar module has a function called month, which allows you to display a calendar for a specific month. Its use is really simple, you just need to specify the year and month - check out the code in the editor
"""
print(calendar.month(2020, 11, l = 2))
calendar.prmonth(2024, 11, w = 2, l = 1) # It doesn't require use print() function to display the calendar



# $ The setfirstweekday() function
""" 
s you already know, by default in the calendar module, the first day of the week is Monday. However, you can change this behavior using a function called setfirstweekday.

Do you remember the table showing the days of the week and their representation in the form of integer values? It's time to use it, because the setfirstweekday method requires a parameter expressing the day of the week in the form of an integer value.
"""
import calendar

calendar.setfirstweekday(calendar.SUNDAY) # | sets the first day of the week to Sunday. It will be the first column in the calendar.
calendar.prmonth(2020, 12) # prints the calendar of December 2020



# $ The weekday() function
""" 
Another useful function provided by the calendar module is the function called weekday, which returns the day of the week as an integer value for the given year, month, and day. Let's see it in practice.
"""
import calendar
print(calendar.weekday(2020, 12, 24)) # - 3 -> Thursday
# check the day of the week that falls on December 24, 2020.



# $ The weekheader() function
""" 
You've probably noticed that the calendar contains weekly headers in a shortened form. If needed, you can get short weekday names using the weekheader method.

The weekheader method requires you to specify the width in characters for one day of the week. If the width you provide is greater than 3, you'll still get the abbreviated weekday names consisting of three characters.

So let's look at how to get a smaller header.
"""

import calendar
print(calendar.weekheader(2)) # | Su Mo Tu We Th Fr Sa
""" 
! Note: If you change the first day of the week, for example, by using the setfirstweekday function, it'll affect the result of the weekheader function
"""


# $ How do we check if a year is a leap-year?
""" 
The calendar module provides two useful functions to check whether years are leap years.

The first one, called isleap, returns True if the passed year is leap, or False otherwise. The second one, called leapdays, returns the number of leap years in the given range of years.
"""
import calendar

print(calendar.isleap(2020)) # - True
print(calendar.leapdays(2010, 2021)) # - 3 -> 2012, 2016, 2020  



# $ Classes for creating calendars
""" 
The functions we've shown you so far aren't everything the calendar module offers. In addition to them, we can use the following classes:

calendar.Calendar; provides methods to prepare calendar data for formatting;
calendar.TextCalendar; is used to create regular text calendars;
calendar.HTMLCalendar; is used to create HTML calendars;
calendar.LocalTextCalendar; is a subclass of the calendar.TextCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.
calendar.LocalHTMLCalendar; is a subclass of the calendar.HTMLCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.
"""

# $ Creating a Calendar object
""" 
The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday).

The firstweekday parameter must be an integer between 0-6. For this purpose, we can use the already-known constants - look at the code in the editor.
"""
import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")



# $ The itermonthdates() method
""" 
he Calendar class has several methods that return an iterator. One of them is the itermonthdates method, which requires specifying the year and month.

As a result, all days in the specified month and year are returned, as well as all days before the beginning of the month or the end of the month that are necessary to get a complete week.

Each day is represented by a datetime.date object.
"""
import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ") # ? it returns all dates in November 2019 plus one more day from december in order to keep the complete week.



# $ Other methods that return iterators
""" 
Another useful method in the Calendar class is the method called itermonthdates, which takes year and month as parameters, and then returns the iterator to the days of the week represented by numbers.
"""
import calendar  

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

""" 
You’ll have certainly noticed the large number of 0s returned as a result of the example code. These are days outside the specified month range that are added to keep the complete week.

The first four zeros represent 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday). The remaining numbers are days in the month, except the last value of 0, which replaces the date 12/01/2019 (Sunday).

There are four other similar methods in the Calendar class that differ in data returned:

itermonthdates2 – returns days in the form of tuples consisting of a day of the month number and a week day number;
itermonthdates3 – returns days in the form of tuples consisting of a year, a month, and a day of the month numbers. This method has been available since Python version 3.7;
itermonthdates4 – returns days in the form of tuples consisting of a year, a month, a day of the month, and a day of the week numbers. This method has been available since Python version 3.7.
"""



# $ The monthdays2calendar() method
# The Calendar class has several other useful methods that you can learn more about in the documentation

# TODO: https://docs.python.org/3/library/calendar.html

""" 
One of them is the monthdays2calendar method, which takes the year and month, and then returns a list of weeks in a specific month. Each week is a tuple consisting of day numbers and weekday numbers. Look at the code in the editor.
"""

import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12): # param1: year, param2: month
    print(data)

""" 
! Note that the day numbers outside the month are represented by 0, while the weekday numbers are a number from 0-6, where 0 is Monday and 6 is Sunday.
"""




# TODO: LAB - The calendar module
""" 
During this course, we took a brief look at the Calendar class. Your task now is to extend its functionality with a new method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

Create a class called MyCalendar that extends the Calendar class;
Create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
In your implementation, use the monthdays2calendar method of the Calendar class.
The following are the expected results:

Sample arguments
year=2019, weekday=0

Expected output
52

Sample arguments
year=2020, weekday=6

Expected output
53
"""


import calendar

class MyCalendar(calendar.Calendar): # extends the Calendar class
    def count_weekday_in_year(self, year, weekday): # takes a year and a weekday as parameters
        current_month = 1 # January
        number_of_days = 0 # number of occurrences of a specific weekday in the year
        while (current_month <= 12): # loop through all months
            for data in self.monthdays2calendar(year, current_month): # get the data for the month
                if data[weekday][0] != 0: # check if the weekday is in the month
                    number_of_days = number_of_days + 1 # increment the number of days

            current_month = current_month + 1 # move to the next month
        return number_of_days # return the number of days

my_calendar = MyCalendar() # create an instance of the MyCalendar class
number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY) # get the number of Mondays in 2019

print(number_of_days) # 52



# $ Section Quiz
import calendar

""" 
Question 1: What is the output of the following snippet?
"""

print(calendar.weekheader(1)) # Su Mo Tu We Th Fr Sa 

""" 
Question 2: What is the output of the following snippet?
"""
c = calendar.Calendar()
 
for weekday in c.iterweekdays():
    print(weekday, end=" ") # 0 1 2 3 4 5 6