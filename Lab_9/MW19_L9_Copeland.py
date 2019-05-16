## Name: T. Emerson Copeland
## MW19   COSC1336   Lab 9  Dictionaries, Sets, Pickling

import pickle

def print_break():
    print("\n=========================================\n")

def state_by_abbrev():

    states_abbrev = {}

    try:
        infile = open('StateCensus2010.txt','r')

        while True:
            state_data = []

            for _ in range(3):
                line = infile.readline()
                line = line.strip()

                if line == "":
                    break
                
                state_data.append(line)
                
            if state_data == []:
                break
            else:
                states_abbrev.update({state_data[1]:state_data[0]})

    except Exception as err:
        print(f"\n=====     Error!     =====\n\nThe following error occurred: {err}")

    else:
        infile.close()

    while True:
        print_break()
        lookup = input("Enter the 2-letter abbreviation you'd like to look up\n"\
            "Enter Q to quit\n\nYour Choice: ")
        
        if lookup.upper() == 'Q':
            print('\nGoodbye!')
            break
        else:
            print(f'\n{states_abbrev.get(lookup.upper(),"Not Found")}')

def set_operations():

    alpha = set()
    for ch in range(ord('a'),ord('a')+26):
        alpha.add(chr(ch))
    
    digits = set(range(0,10))

    even = set()
    for num in digits:
        if num%2==0:
            even.add(num)
    
    vowels = set('aeiou')     # and sometimes y  :-)

    punct = set('''~`!@#$%^&*()_-+={[}]|\\:;'"<,>.?/''')

    match = set('{}[]()<>')

    advice = set('treat others kindly')

    address = set('11928 stonehollow dr., austin, tx (us [of] a)')

    print_break()
    print(f'\nConsonants: {alpha.difference(vowels)}')
    print(f'\nOdds: {digits.difference(even)}')
    print(f'\nAdvice_Consonant: {advice.difference(vowels)}')
    
    ## Must convert string version of digits in address to int version and store in own set
    address_chars = set()
    for char in address:
        if char.isdigit():
            char = int(char)
            address_chars.add(char)

    print(f'\nOdd_Address: {address_chars.intersection(digits.difference(even))}')
    print(f'\nPunct_Address: {address.intersection(punct)}')
    print(f'\nNo_Match: {address.intersection(punct.difference(match))}')

def pickle_play():

    end_of_file = False

    try:
        infile = open('secret.dat', 'rb')

        while not end_of_file:
            try:
                data = pickle.load(infile)
                print(data)
                print_break()
            except EOFError:
                end_of_file = True

    except Exception as err:
        print(f"\n=====     Error!     =====\n\nThe following error occurred: {err}")

    else:
        infile.close()
def menu():
    while True:
        print_break()
        choice = input('Which part would you like to do?\nEnter 1, 2, 3, or Q to quit: ')
    
        if choice.upper() == 'Q':
            print('\nGoodbye!')
            break
        elif choice == '1':
            state_by_abbrev()
        elif choice == '2':
            set_operations()
        elif choice == '3':
            pickle_play()
        else:
            print('Invalid Choice')

menu()


## Test Data:
# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_9 (master)
# $ python MW19_L9_Copeland.py

# =========================================

# Which part would you like to do?
# Enter 1, 2, 3, or Q to quit: 1

# =========================================

# Enter the 2-letter abbreviation you'd like to look up
# Enter Q to quit

# Your Choice: PA

# Pennsylvania

# =========================================

# Enter the 2-letter abbreviation you'd like to look up
# Enter Q to quit

# Your Choice: wy

# Wyoming

# =========================================

# Enter the 2-letter abbreviation you'd like to look up
# Enter Q to quit

# Your Choice: oR

# Oregon

# =========================================

# Enter the 2-letter abbreviation you'd like to look up
# Enter Q to quit

# Your Choice: Ca

# California

# =========================================

# Enter the 2-letter abbreviation you'd like to look up
# Enter Q to quit

# Your Choice: q

# Goodbye!

# =========================================

# Which part would you like to do?
# Enter 1, 2, 3, or Q to quit: 2

# =========================================


# Consonants: {'g', 'k', 'r', 'p', 'q', 'h', 'b', 'w', 'v', 's', 'f', 'l', 'd', 'n', 'j', 'y', 't', 'm', 'x', 'z', 'c'}

# Odds: {1, 3, 5, 7, 9}

# Advice_Consonant: {'s', 'k', 'l', 'd', 'r', 'n', 'y', ' ', 't', 'h'}

# Odd_Address: {1, 9}

# Punct_Address: {']', '[', '.', '(', ')', ','}

# No_Match: {'.', ','}

# =========================================

# Which part would you like to do?
# Enter 1, 2, 3, or Q to quit: 3
# The mists of time run thick and thin.

# =========================================

# {1: 'George', 'by': ['G', 'e', 'o', 'r', 'g', 'e'], 'George': 'name', 41: 'George', 43: 'George', 'Foreman': (5, 'George')}

# =========================================

# [[[[[['deep'], 'in'], 'the'], 'heart'], 'of'], 'Texas']

# =========================================

# {True, 3, 'hash-me', ('zip', 'code'), 'egg', (90210, 20500, 10001), 123.456}

# =========================================

# 5

# =========================================


# =========================================

# Which part would you like to do?
# Enter 1, 2, 3, or Q to quit: q

# Goodbye!

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_9 (master)
# $
