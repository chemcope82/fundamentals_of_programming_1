##  Name:  T. Emerson Copeland
##  COSC 1336   MW19 

import random

def print_break():
    print("\n=========================================\n")

def get_filename():
    file_name = input("\nPlease enter the file name: ")
    
    if not file_name.endswith('.txt'):
        file_name = file_name + ".txt"
    
    return file_name

def createData(file_name,randCount):
    try:
        numberFile = open(file_name, 'w')
    except:
        return False
    else:
        counter = 0

        while counter < randCount:
            numberFile.write(str(random.randint(1,1000))+" ")
            counter += 1
        
        numberFile.close()
        return True
        
def evenodd(num):
    return not num%2


def showData(filename):
    list_of_numbers = []
    try:
        infile = open(filename, 'r')
    except:
        return False
    else:
        while True:
            line = infile.readline()
            if line == "":
                break
            else:
                for num in line.split():
                    list_of_numbers.append(num)
        
    for num in list_of_numbers:
        try:
            num = int(num)
        except:
            pass
        else:
            if evenodd(num):
                print(f"{num} is even")
            else:
                print(f"{num} is odd")
    
    return True


def menu():
    while True:
        print_break()
        user_choice = input("Please choose what you'd like to perform:\n\nC) Create a file with random numbers\n"\
        "V) View the file contents\nQ) Quit\n\nYour choice: ")
        
        if user_choice[0].lower() == 'q':
            break
        elif user_choice[0].lower() == 'c':
            print_break()
            print('This option will let you write random numbers to a file.\n')
            file_name = get_filename()
            while True:
                try:
                    randCount = int(input("\nHow many random numbers do you want to create? "))
                except ValueError:
                    print('\nSorry, you must enter an integer')
                else:
                    break
            if createData(file_name,randCount):
                print_break()
                print(f"\nSuccess! {file_name} was created")
            else:
                print_break()
                print(f"\nDisaster! {file_name} could not be created!")

        elif user_choice[0].lower() == 'v':
            print('This option will let you view the contents of a file.\n')
            file_name = get_filename()
            if not showData(file_name):
                print_break()
                print(f"\nDisaster! Something went wrong when I tried to read from {file_name}!")

        else:
            print_break()
            print("I'm sorry, I didn't understand that.  Please try again")

menu()


# Test Data:
# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Exam_2_Lab (master)
# $ python MW19_X2p3_Copeland.py

# =========================================

# Please choose what you'd like to perform:

# C) Create a file with random numbers
# V) View the file contents
# Q) Quit

# Your choice: c

# =========================================

# This option will let you write random numbers to a file.


# Please enter the file name: some_numbers

# How many random numbers do you want to create? 25

# =========================================


# Success! some_numbers.txt was created

# =========================================

# Please choose what you'd like to perform:

# C) Create a file with random numbers
# V) View the file contents
# Q) Quit

# Your choice: c

# =========================================

# This option will let you write random numbers to a file.


# Please enter the file name: some_more_numbers::txt

# How many random numbers do you want to create? 10

# =========================================


# Disaster! some_more_numbers::txt.txt could not be created!

# =========================================

# Please choose what you'd like to perform:

# C) Create a file with random numbers
# V) View the file contents
# Q) Quit

# Your choice: v
# This option will let you view the contents of a file.


# Please enter the file name: some_numbers
# 992 is even
# 409 is odd
# 429 is odd
# 667 is odd
# 759 is odd
# 162 is even
# 449 is odd
# 592 is even
# 285 is odd
# 719 is odd
# 808 is even
# 646 is even
# 861 is odd
# 939 is odd
# 692 is even
# 652 is even
# 273 is odd
# 220 is even
# 837 is odd
# 16 is even
# 304 is even
# 746 is even
# 834 is even
# 44 is even
# 482 is even

# =========================================

# Please choose what you'd like to perform:

# C) Create a file with random numbers
# V) View the file contents
# Q) Quit

# Your choice: v
# This option will let you view the contents of a file.


# Please enter the file name: something_other_than_numbers

# =========================================


# Disaster! Something went wrong when I tried to read from something_other_than_numbers.txt!

# =========================================

# Please choose what you'd like to perform:

# C) Create a file with random numbers
# V) View the file contents
# Q) Quit

# Your choice: q

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Exam_2_Lab (master)
# $
