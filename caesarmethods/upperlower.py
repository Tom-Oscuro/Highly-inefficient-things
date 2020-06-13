### CAESAR CIPHER USING THE FULL ASCII TABLE IN ONE LINE ###

### VARIABLES ###
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
plaintext = ""
shiftvalue = 0
plaintextlen = 0
upperlen = 0
lowerlen = 0
ciphertext = ''

### DEFINING FUNCTIONS ###

def inputvalues():
    global plaintext
    global shiftvalue
    global plaintextlen
    global upperlen
    global lowerlen
    plaintext = input('\nPlaintext: ')
    shiftvalue = int(input('\nShift value: '))
    plaintextlen = len(plaintext)
    upperlen = len(upper_alphabet)
    lowerlen = len(lower_alphabet)

def solve():
    global ciphertext
    for i in range(plaintextlen):
        character = plaintext[i]
        if character in upper_alphabet:
            location = upper_alphabet.find(character)
            new_location = (location + shiftvalue) % upperlen
            ciphertext += upper_alphabet[new_location]
        elif character in lower_alphabet:
            location = lower_alphabet.find(character)
            new_location = (location + shiftvalue) % lowerlen
            ciphertext += lower_alphabet[new_location]
        elif character in numbers:
            location = numbers.find(character)
            new_location = (location + shiftvalue) % 10
            ciphertext += numbers[new_location]
        else:
            ciphertext += character

def separator():
    print('\n------------------------------')

def again():
    again = input('\nAgain? (Y / N)  ')
    while again not in ['Y', 'N', 'y', 'n']:
        again = input('\nAgain? (Y / N)  ')
    if again == 'Y' or again == 'y':
        start()
    else:
        pass

def start():
    global ciphertext
    inputvalues()
    solve()
    print(f'\nCiphertext: {ciphertext}')
    separator()
    ciphertext = ''
    again()
