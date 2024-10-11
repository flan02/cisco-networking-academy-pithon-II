
# TODO: String methods

# ? String methods are functions that operate on strings and can be used to manipulate their contents.

# - the capitalize() method returns a copy of the string with its first character capitalized and the rest lowercased.
print('aBcD'.capitalize()) # Abcd

# - the center() method returns a copy of the string, padded with spaces or any other character to make it centered.
print('[' + 'alpha'.center(10) + ']') # [  alpha   ]
print('[' + 'gamma'.center(20, '*') + ']') # [*******gamma********]
print('[' + 'gamma'.center(10, '!') + ']') # [!!gamma!!!]

# - the endswith() method returns True if the string ends with the specified suffix, otherwise it returns False.