## Name: T. Emerson Copeland
## MW19   COSC1336   Lab 8

import string
import random

def print_break():
    print("\n=========================================\n")

password_attempts = 0

def validate_password(pwd=''):

    global password_attempts
    password_attempts += 1

    correct_length = False  #8 characters or more
    has_space = False   #No spaces
    has_digit = False   #At least one digit
    has_punct = False   #At least one punctuation
    has_2Upper = False   #At least 2 uppercase
    has_2Lower = False   #At least 2 lowercase
    num_caps = 0
    num_lower = 0

    if len(pwd) >= 8:
        correct_length = True

        for char in pwd:
            if char.isspace():
                has_space = True
            
            if char.isdigit():
                has_digit = True

            if char in string.punctuation:
                has_punct = True

            if num_caps < 2:
                if char.isupper():
                    num_caps += 1
            else: has_2Upper = True

            if num_lower < 2:
                if char.islower():
                    num_lower += 1
            else: has_2Lower = True

    if correct_length and not has_space and has_digit and \
        has_punct and has_2Upper and has_2Lower:
        return True
    else:
        return False

def get_password():
    print_break()
    pwd = input('Please enter a password.\nPasswords must be at least 8 characters in length, and contain the following:\n'+\
        '2 upper case letters\n2 lower case letters\n1 punctuation character\n1 digit\nNo spaces\n\n>>> ')
    return pwd

def generate_password():
    ## ASCII Printable Characters:
    ## punctuation: 33-47, 58-64, 91-96, 123-126
    ## Cap Letters: 65-90
    ## Lower Letters: 97-122
    ## Digits: 48-57
    pass_length = random.randint(8,21) # Password length between 8 and 20 characters
    pwd_list = [] # List to hold password characters
    punct_list = [] # List to hold punctuation options
    punct_list.extend(range(33,48))
    punct_list.extend(range(58,65))
    punct_list.extend(range(91,97))
    punct_list.extend(range(123,127))

    # Add 1 punctuation, 1 digit, 2 upper case, and 2 lower case characters to password list
    pwd_list.append(chr(random.choice(punct_list))) 
    pwd_list.append(chr(random.choice(range(48,58))))
    pwd_list.append(chr(random.choice(range(65,91))))
    pwd_list.append(chr(random.choice(range(65,91))))
    pwd_list.append(chr(random.choice(range(97,123))))
    pwd_list.append(chr(random.choice(range(97,123))))

    # Continue adding to password list until it is the specified length
    while len(pwd_list) < pass_length:
        pwd_list.append(chr(random.choice(range(33,127))))
    
    random.shuffle(pwd_list) # Shuffle the random characters in the password list

    pwd = "".join(pwd_list) # Convert the password list into a string

    return pwd


while True:

    if password_attempts > 2:
        print_break()
        print("It seems like you're having trouble.  I'll help you make a password:\n")
        print(f"{generate_password()}")
        break

    if validate_password(get_password()):
        print("\n===   Success!  Your password has been set.   ===")
        break
    else:
        print_break()
        print("\n===   Oh no! Your password didn't meet the criteria.   ===")

print(f"\nYou tried {password_attempts} times to set your password")

