### CAESAR CIPHER USING THE FULL ASCII TABLE IN ONE LINE ###

### VARIABLES ###
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
plaintext = ""
shiftvalue = 0
plaintextlen = 0
alphalen = 0
ciphertext = ''

### DEFINING FUNCTIONS ###

def inputvalues():
    global plaintext
    global shiftvalue
    global plaintextlen
    global alphalen
    plaintext = input('\nPlaintext: ')
    plaintext = plaintext.upper()
    shiftvalue = int(input('\nShift value: '))
    plaintextlen = len(plaintext)
    alphalen = len(alphabet)

def solve():
    global ciphertext
    for i in range(plaintextlen):
        character = plaintext[i]
        if character in alphabet:
            location = alphabet.find(character)
            new_location = (location + shiftvalue) % alphalen
            ciphertext += alphabet[new_location]
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
