
# TODO: FOUR SIMPLE PROGRAMS

# $1 The Caesar Cipher: encrypting a message
#  https://en.wikipedia.org/wiki/Caesar_cipher

text = input("Enter your message: ") # "hello" # "ave caesar"
cipher = ''
for char in text:
    if not char.isalpha(): # ignore non-alphabetic characters
        continue # skip to the next iteration
    char = char.upper() # convert to uppercase
    code = ord(char) + 1 # shift by 1
    if code > ord('Z'): # wrap around
        code = ord('A') # go back to 'A'
    cipher += chr(code) # append the encrypted character

print(cipher) # "IFMMP" # "BWFDBFTBS"

# $2 The Caesar Cipher: decrypting a message

cipher = input('Enter your cryptogram: ') # "IFMMP" # "BWFDBFTBS"
text = ''
for char in cipher:
    if not char.isalpha(): # ignore non-alphabetic characters
        continue # skip to the next iteration
    char = char.upper() # convert to uppercase
    code = ord(char) - 1 # shift by -1
    if code < ord('A'): # wrap around
        code = ord('Z') # go back to 'Z'
    text += chr(code)

print(text) # "HELLO" # "AVECAESAR"



# $3 The Numbers Processor

line = input("Enter a line of numbers - separate them with spaces: ") # "1 2 3 4 5"
strings = line.split() # ["1", "2", "3", "4", "5"]
total = 0 # accumulator
try:
    for substr in strings: # "1", "2", "3", "4", "5"
        total += float(substr) # 1, 3, 6, 10, 15
    print("The total is:", total) # 15
except:
    print(substr, "is not a number.") 



# $4 The IBAN Validator (international back account number)

iban = input("Enter IBAN, please: ") # "GB72 HBZU 7006 7212 1253 00"
iban = iban.replace(' ','') # "GB72HBZU70067212125300"

if not iban.isalnum(): # check if all characters are alphanumeric
    print("You have entered invalid characters.") 
elif len(iban) < 15: # check the minimum length
    print("IBAN entered is too short.")
elif len(iban) > 31: # check the maximum length
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper() # move the first four characters to the end
    iban2 = '' # accumulator
    for ch in iban: # "HBZU70067212125300GB72"
        if ch.isdigit(): # check if the character is a digit
            iban2 += ch # append the digit
        else: # convert the letter to two digits
            iban2 += str(10 + ord(ch) - ord('A')) # append the digit code
    iban = int(iban2) # convert the string to an integer
    if iban % 97 == 1: # check if the IBAN is valid
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.") 



# $ The Caesar Cipher -> Improved

text = input("Enter message: ") # The die is cast

# Enter a valid shift value (repeat until it succeeds).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter the cipher shift value (1..25): ")) # 25
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect shift value!")

cipher = ''

for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Make correction.
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char

print(cipher) #  Sgd chd hr bzrs
    


# $ Extra - Palindromes
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

text = input("Enter text: ") # baab

# Remove all spaces...
text = text.replace(' ','')

# ... and check if the word is equal to reversed itself
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("It's a palindrome") # It's a palindrome
else:
	print("It's not a palindrome") # It's not a palindrome
    

# $ Extra - Sudoku

# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Check if all columns are good.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Make a string containing all digits from a sub-square.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")