

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

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1]) # are


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

s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2) # ValueError: invalid literal for int() with base 10: '12.8'


""" 
string == number is always False;
string != number is always True;
string >= number always raises an exception.
"""




# TODO: LAB a LED Display

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Enter the number you wish to display: ")))