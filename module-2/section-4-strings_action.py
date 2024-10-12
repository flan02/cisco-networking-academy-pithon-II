

# $ COMPARING STRINGS

'alpha' == 'alpha' # True
'alpha' != 'Alpha' # True

'alpha' < 'alphabet' # True

# * The comparison is case-sensitive, and the lowercase letters are considered greater than the uppercase letters.
'beta' > 'Beta' # True

print('10' == '010') # False
print('10' > '010') # True
print('10' > '8') # False
print('20' < '8') # True
print('20' < '80') # True

# ! Comparing strings against numbers is generally a bad idea.
print('10' == 10) # False
print('10' != 10) # True
print('10' == 1) # False
print('10' != 1) # True
#print('10' > 1) # TypeError: '>' not supported between instances of 'str' and 'int'


# $ SORTING STRINGS

greek = ['omega', 'alpha', 'pi', 'gamma']

# TODO: The sorted() function returns a new list containing all items from the original list in the sorted order.
greek_sorted = sorted(greek)

print(greek) # ['omega', 'alpha', 'pi', 'gamma']
print(greek_sorted) # ['alpha', 'gamma', 'omega', 'pi']

# TODO: The sort() method sorts the list in place. No new list is created.
new_greek = ['omega', 'alpha', 'pi', 'gamma']

print(new_greek) # ['omega', 'alpha', 'pi', 'gamma'] 
new_greek.sort()
print(new_greek) # ['alpha', 'gamma', 'omega', 'pi']   


# $ STRINGS vs NUMBERS

""" 
There are two additional issues that should be discussed here: how to convert a number (an integer or a float) into a string, and vice versa. It may be necessary to perform such a transformation. Moreover, it's a routine way to process input/output data.

The number-string conversion is simple, as it is always possible. It's done by a function named str().
"""
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf) # 13 1.3

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt) # 14.3