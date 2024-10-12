
# TODO: String methods

# ? String methods are functions that operate on strings and can be used to manipulate their contents.

# - the capitalize() method returns a copy of the string with its first character capitalized and the rest lowercased.
print('aBcD'.capitalize()) # Abcd

# - the center() method returns a copy of the string, padded with spaces or any other character to make it centered.
print('[' + 'alpha'.center(10) + ']') # [  alpha   ]
print('[' + 'gamma'.center(20, '*') + ']') # [*******gamma********]
print('[' + 'gamma'.center(10, '!') + ']') # [!!gamma!!!]

# - the endswith() method returns True if the string ends with the specified suffix, otherwise it returns False.
if "epsilon".endswith("on"):
    print("yes") # yes
else:
    print("no") 

t = "zeta"
print(t.endswith("a")) # True
print(t.endswith("A")) # False
print(t.endswith("et")) # False
print(t.endswith("eta")) # True

# - the find() method returns the lowest index in the string where the specified substring is found. If the substring is not found, the method returns -1.
print("Eta".find("ta")) # 1
print("Eta".find("mma")) # -1
""" 
Note: don't use find() if you only want to check if a single character occurs within a string - the in operator will be significantly faster.
"""
t = 'theta'
print(t.find('eta')) # 2
print(t.find('et')) # 2
print(t.find('the')) # 0
print(t.find('ha')) # -1

print('kappa'.find('a', 2)) # 4

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd) # 15, 80, 198, 221, 238
    fnd = the_text.find('the', fnd + 1) # finds all occurrences of 'the' in the_text

print('kappa'.find('a', 1, 4)) # 1
print('kappa'.find('a', 2, 4)) # -1


# - the isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers), otherwise e.g. (* , _ , /, ' ') it returns False.
print('lambda30'.isalnum()) # True
print('lambda'.isalnum()) # True
print('30'.isalnum()) # True
print('@'.isalnum()) # False
print('lambda_30'.isalnum()) # False
print(''.isalnum()) # False

t = 'Six lambdas' # space character
print(t.isalnum()) # False

t = '&Alpha;&beta;&Gamma;&delta;' # non-alphanumeric characters
print(t.isalnum()) # False

t = '20E1'
print(t.isalnum()) # True


# - the isalpha() method returns True if all characters in the string are alphabetic, otherwise it returns False.
print("Moooo".isalpha()) # True
print('Mu40'.isalpha()) # False


# - the isdigit() method returns True if all characters in the string are digits, otherwise it returns False.
print('2018'.isdigit()) # True
print("Year2019".isdigit()) # False


# - the islower() method returns True if all alphabetic characters in the string are lowercase, otherwise it returns False.
print("Moooo".islower()) # False
print('moooo'.islower()) # True


# - the isspace() method returns True if all characters in the string are whitespaces, otherwise it returns False.
print(' \n '.isspace()) # True
print(" ".isspace()) # True
print("mooo mooo mooo".isspace()) # False


# - the isupper() method returns True if all alphabetic characters in the string are uppercase, otherwise it returns False.
print("Moooo".isupper()) # False
print('moooo'.isupper()) # False
print('MOOOO'.isupper()) # True


# - the join() method returns a string created by joining the elements of an iterable using the specified separator.
print(",".join(["omicron", "pi", "rho"])) # omicron,pi,rho

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list) 
print(s) # Where*are*the*snows?


# - the lower() method returns a copy of the string converted to lowercase.
# * Note: It's works like lowerCase() in JavaScript.
print("SiGmA=60".lower()) # sigma=60


# - the lstrip() method returns a copy of the string with leading characters removed (based on the string argument passed).
# * Note: It's works like trimLeft() in JavaScript.
print("[" + " tau ".lstrip() + "]") # [tau ]
print("www.cisco.com".lstrip("w.")) # cisco.com
print("pythoninstitute.org".lstrip(".org")) # pythoninstitute.org


# - the replace() method returns a copy of the string with all occurrences of the old substring replaced by the new substring.
# * Note: It's works like replace() in JavaScript.
print("I feel, I feel, I feel more than I realize".replace("feel", "felt")) # I felt, I felt, I felt more than I realize
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) # www.pythoninstitute.org
print("Apple juice".replace("juice", "")) # Apple

# ? The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
print("This is it!".replace("is", "are", 1)) # Thare is it!
print("This is it!".replace("is", "are", 2)) # Thare are it!

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s) # It is either hard or possible


# - the rfind() method returns the highest index in the string where the specified substring is found, or -1 if the substring is not found.
# * Note: It's works like lastIndexOf() in JavaScript.
print("tau tau tau".rfind("ta")) # 8
print("tau tau tau".rfind("ta", 9)) # 8
print("tau tau tau".rfind("ta", 3, 9)) # 4


# - the rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed).
# * Note: It's works like trimRight() in JavaScript.
print("[" + " upsilon ".rstrip() + "]") # [ upsilon]
print("cisco.com".rstrip(".com")) # cisco


# - the split() method returns a list of substrings separated by the specified delimiter.
# * Note: It's works like split() in JavaScript.
print("phi       chi\npsi".split()) # ['phi', 'chi', 'psi']

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split() # ['Where', 'are', 'the', 'snows', 'of', 'yesteryear?']
print(s2[-2]) # of
# ? The split() method can take an optional second argument called maxsplit, which specifies how many splits to do.
# ! Note: the reverse operation can be performed by the join() method.


# - the startswith() method returns True if the string starts with the specified prefix, otherwise it returns False.
# * Note: It's works like startsWith() in JavaScript.
print("omega".startswith("meg")) # False
print("omega".startswith("om")) # True


# - the strip() method returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).
# * Note: It's works like trim() in JavaScript.
print("[" + "   aleph   ".strip() + "]") # [aleph]


# - the swapcase() method returns a copy of the string with uppercase characters converted to lowercase and vice versa.
print("I know that I know nothing.".swapcase()) # i KNOW THAT i KNOW NOTHING.


# - the title() method returns a copy of the string with the first character of each word capitalized and the rest lowercased.
print("I know that I know nothing. Part 1.".title()) # I Know That I Know Nothing. Part 1.


# - the upper() method returns a copy of the string converted to uppercase.
# * Note: It's works like toUpperCase() in JavaScript.
print("I know that I know nothing. Part 2.".upper()) # I KNOW THAT I KNOW NOTHING. PART 2.


# - the zfill() method returns a copy of the string filled with leading zeros.
print("42".zfill(5)) # 00042

# $ SUMMARY:
""" 
1. Some of the methods offered by strings are:

capitalize(): changes all string letters to capitals;
center(): centers the string inside the field of a known length;
count(): counts the occurrences of a given character;
join(): joins all items of a tuple/list into one string;
lower(): converts all the string's letters into lower-case letters;
lstrip(): removes the white characters from the beginning of the string;
replace(): replaces a given substring with another;
rfind(): finds a substring starting from the end of the string;
rstrip(): removes the trailing white spaces from the end of the string;
split(): splits the string into a substring using a given delimiter;
strip(): removes the leading and trailing white spaces;
swapcase(): swaps the letters' cases (lower to upper and vice versa)
title(): makes the first letter in each word upper-case;
upper(): converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):

endswith(): does the string end with a given substring?
isalnum(): does the string consist only of letters and digits?
isalpha(): does the string consist only of letters?
islower(): does the string consists only of lower-case letters?
isspace(): does the string consists only of white spaces?
isupper(): does the string consists only of upper-case letters?
startswith(): does the string begin with a given substring?
"""