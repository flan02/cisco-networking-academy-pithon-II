
# $ Strings in Python are immutable sequences of characters.
# Strings are sequences of characters, which are effectively stored in memory as an array of characters.
# - https://docs.python.org/3.4/library/stdtypes.html#string-methods 

# e.g. 1
word = 'by'
print(len(word)) # 2


# e.g. 2
empty = ''
print(len(empty)) # 0


# e.g. 3
i_am = 'I\'m'
print(len(i_am)) # 3

multiline = '''Line #1
Line #2'''

print(len(multiline)) # 15

# -----------------------------------------------

str1 = 'a'
str2 = 'b'

print(str1 + str2) # ab
print(str2 + str1) # ba
print(5 * 'a') # aaaaa
print('b' * 4) # bbbb

# -----------------------------------------------

# ? Demonstrating the ord() function.
# ? The ord() function returns the number representing the unicode code of a specified character.
char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1)) # 97
print(ord(char_2)) # 32

# -----------------------------------------------

# ? Demonstrating the chr() function.
# ? The chr() function returns the character that represents the specified unicode code.

print(chr(97)) # a
print(chr(94)) # ^

for ch in "abc":
    print(chr(ord(ch) + 1), end='') # bcd

#chr(ord(x)) == x 
#ord(chr(x)) == x 

# -----------------------------------------------

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print() # s i l l y   w a l k s

for character in the_string:
    print(character, end=' ')

print() # s i l l y   w a l k s

# -----------------------------------------------

# Slices

alpha = "abdefg"

print(alpha[1:3]) # bd
print(alpha[3:]) # efg
print(alpha[:3]) # abd
print(alpha[3:-2]) # e
print(alpha[-3:4]) # e
print(alpha[::2]) # adg
print(alpha[1::2]) # beg

# -----------------------------------------------

# ? The IN and NOT IN operators. It looks similar than includes() in JavaScript.

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet) # True
print("F" in alphabet) # False
print("1" in alphabet) # False
print("ghi" in alphabet) # True
print("Xyz" in alphabet) # False

print("f" not in alphabet) # False
print("F" not in alphabet) # True
print("1" not in alphabet) # True
print("ghi" not in alphabet) # False
print("Xyz" not in alphabet) # True


alphabet = "abcdefghijklmnopqrstuvwxyz"
#del alphabet[0] # ! TypeError: 'str' object doesn't support item deletion
#del alphabet # it works

alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet.append("A") # ! AttributeError: 'str' object has no attribute 'append'
#alphabet.insert(0, "A") # ! AttributeError: 'str' object has no attribute 'insert' 

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet # adds "a" at the beginning of the string
alphabet = alphabet + "z" # adds "z" at the end of the string

print(alphabet) # abcdefghijklmnopqrstuvwxyza

# $ IMPORTANT
""" 
You may want to ask if creating a new copy of a string each time you modify its contents worsens the effectiveness of the code.
Yes, it does. A bit. It's not a problem at all, though.
"""

# -----------------------------------------------
# ? min() searchs for the smallest element in the string. Smallest means the character with the smallest unicode code.

#  Demonstrating min() - e.g 1:
print(min("aAbByYzZ")) # A 


#  Demonstrating min() - ee.gg. 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']') # [ ] 

t = [0, 1, 2]
print(min(t)) # 0 


# ? max() has the opposite effect to min(). It returns the character with the highest unicode code.

#  Demonstrating max() - e.g. 1:
print(max("aAbByYzZ")) # z


#  Demonstrating max() - ee.gg. 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']') # [y]

t = [0, 1, 2]
print(max(t)) # 2

# -----------------------------------------------
# ? The index() method searches the sequence from the beginning, in order to find the first element of the value specified in its argument.

#  Demonstrating the index() method:
print("aAbByYzZaA".index("b")) # 2
print("aAbByYzZaA".index("Z")) # 7
print("aAbByYzZaA".index("A")) # 1
print("aAbByYzZaA".index("a")) # 0

# -----------------------------------------------
# ? The list() function creates a list from its argument.

#  Demonstrating the list() function:
print(list("abcabc")) # ['a', 'b', 'c', 'a', 'b', 'c']

# -----------------------------------------------
# ? The count() method counts all occurrences of the element inside the sequence.

#  Demonstrating the count() method:
print("abcabc".count("a")) # 2
print("abcabc".count("b")) # 2 
print("abcabc".count("d")) # 0