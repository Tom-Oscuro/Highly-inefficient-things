### CAESAR PROGRAM ###
from caesarmethods import fullascii
from caesarmethods import simplecaesar
from caesarmethods import caesarwithnumbers
from caesarmethods import upperlower

### VARIABLES ###
choice = 0
valid_options = [1, 2, 3, 4, 5]

### DEFINING FUNCTIONS ###
def lista():
    print('- 1 - SIMPLE CAESAR (A-Z)\n' +
          '- 2 - CAESAR WITH NUMBERS (A-Z, 0-9)\n' +
          '- 3 - CAESAR WITH LOWER AND UPPER CASE PLUS NUMBERS (a-z, A-Z, 0-9)\n' +
          '- 4 - FULL ASCII CAESAR\n' +
          '- 5 - Other options will be available later.\n')

def run():
    global choice
    print('CHOSE A METHOD FROM BELOW:')
    lista()
    choice = int(input('Your choice: '))
    while choice not in valid_options:
        print('That was never a valid option. Choose something from the list!')
        lista()
        choice = int(input('Your choice: '))
    method_list()
    again()

# Solving methods
def method_list():
    if choice == 1:
        simplecaesar_solve()
    elif choice == 2:
        caesarwithnumbers_solve()
    elif choice == 3:
        upperlower_solve()
    elif choice == 4:
        fullascii_solve()
    elif choice == 5:
        print ('\nI SAID LATER!!! You little tryhard! xP\n')

def simplecaesar_solve():
    separator()
    print('\nTHIS ONLY USES THE STANDARD ENGLISH APHABET (A-Z)\n' +
          "NOT CASE SENSITIVE, DOEN'T UNDERSTANDS NUMBERS\n")
    simplecaesar.start()

def caesarwithnumbers_solve():
    separator()
    print('\nTHIS USES THE ENGLISH APHABET (A-Z) AND NUMBERS (0-9)\n' +
          "NOT CASE SENSITIVE, UNDERSTANDS NUMBERS\n")
    caesarwithnumbers.start()

def upperlower_solve():
    separator()
    print('\nTHIS USES THE ENGLISH APHABET (A-Z) AND NUMBERS (0-9)\n' +
          "CASE SENSITIVE, UNDERSTANDS NUMBERS")
    upperlower.start()

def fullascii_solve():
    separator()
    print('\nWITH THIS YOU CAN SHIFT USING THE FULL ASCII TABLE IN ONE LINE')
    fullascii.start()
# End Solving methods

def separator():
    print('\n------------------------------\n')

# Restart cycle
def again():
    again = input('\nDo you want to try something else? (Y / N)  ')
    while again not in ['Y', 'N', 'y', 'n']:
        again = input('\nDo you want to try something else? (Y / N)  ')
    if again == 'Y' or again == 'y':
        separator()
        run()
    else:
        separator()
        print('\nThanks for trying this program!\n' +
              '\nYou can close the window...\n')

### RUN THE ACTUAL PROGRAM ###
separator()
print('Greetings!\n')
run()
