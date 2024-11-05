
my_list = [1, 2, 3]
# Insert line of code here.

#foo = [x**x for x in my_list] # it returns a list
#foo = list(map(lambda x: x**x, my_list)) # it returns a list
foo = tuple(map(lambda x: x**x, my_list)) # it returns a tuple
print(foo) # | 1, 4, 27


my_tuple = (0, 1, 2, 3, 4, 5, 6)
# Insert line of code here.
foo = list(filter(lambda x: x-0 and x-1, my_tuple)) 
print(foo) # [2, 3, 4, 5, 6]



def I():
    s = 'abcdef'
    for c in s[::2]: # What does this do? -> it returns every second character of the string
        yield c


for x in I(): 
    print(x, end='') # | ace



def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x, end='') # | ++++++




def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s()) # | ***




# errno.EEXIST  # it means that the file already exists



b = bytearray(3)
print(b) # | bytearray(b'\x00\x00\x00')





import os

os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('thumbnails')
os.chdir('thumbnails')
os.mkdir('tmp')
os.chdir('../')

print(os.getcwd()) # | /home/runner/pictures/thumbnails




import os

os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)

print(os.listdir()) # | ['small', 'medium', 'large']




from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2) # | 345 days, 0:00:00




from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S')) # 2019/Nov/27 11:27:22




import calendar
print(calendar.weekheader(2)) # | Mo Tu We Th Fr Sa Su




import calendar

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ") # | 0 1 2 3 4 5 6

