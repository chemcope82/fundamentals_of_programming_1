# Name: T. Emerson Copeland     MW19
# COSC1336  Lab 7

name_list = []

def print_break():
    print("\n=========================================\n")

def get_filename():
    file_name = input("\nPlease enter the file name: ")
    
    if not file_name.endswith('.txt'):
        file_name = file_name + ".txt"
    
    return file_name

def read_file():
    some_list = []
    try:
        infile = open(get_filename(), 'r')
        for line in infile:
            line = line.rstrip("\n")
            some_list.append(line)
    
    except Exception as err:
        print(f"\n=====     Error!     =====\n\nThe following error occurred: {err}")
    else:
        infile.close()
        print("\nYour file was successfully read.")
        return some_list

def write_file(some_list):
    print("You must enter a file name to write to.")
    try:
        outfile = open(get_filename(), 'w')
        for item in some_list:
            outfile.write(item + "\n")
        
    except Exception as err:
        print(f"\n=====     Error!     =====\n\nThe following error occurred: {err}")

    else:
        outfile.close()
        print("\nYour file was successfully written.")
def view_list(some_list):
    for index, item in enumerate(some_list, 1):
        print(f"{index}) {item}, ", end="")
        if (index % 10 == 0):
            print("\n")

def insert_name(some_list):
    name = input("\nWhat name would you like to insert in the list? ")
    if find_name(name, some_list):
        print(f"\n{name.capitalize()} is already in the list")
        return
    try:
        index = int(input("\nAt what position number would you like to insert the name? "))
    except ValueError:
        print(f"\n=====     Error!     =====\n\nThe following error occurred:")
        print("\nYou must enter a number for the position")
    else:
        some_list.insert(index-1, name.capitalize())
        if index < len(some_list):
            print(f"\n{name.capitalize()} has been inserted at position {index}")
        else:
            print(f"\n{name.capitalize()} has been inserted at the end of the list.")

def find_name(name, some_list):
    return name.capitalize() in some_list

def delete_name(name, some_list):
    if find_name(name, some_list):
        del some_list[some_list.index(name.capitalize())]
        print(f"\n{name.capitalize()} was deleted from the list.")
    else:
        print(f"\n{name.capitalize()} is not in the list.")

def menu():

    while True:
        print_break()
        user_choice = input("Please choose what you'd like to perform:\n\nR) Read File\nW) Write to File\n" \
        "I) Insert in File\nD) Delete from File\nF) Find in File\nS) Sort a File\nV) View Contents of File\nQ) Quit\n\nYour choice: ")
        user_choice = user_choice.upper()

        if user_choice == "Q":
            break

        elif user_choice == "R":
            print_break()
            print("\nThis option will read a file into a list for you.")
            name_list = read_file()

        elif user_choice == "W":
            print_break()
            print("\nThis option will write your current list into a new file for you.")
            write_file(name_list)

        elif user_choice == "I":
            print_break()
            print("\nThis option will allow you to insert a name into the list.")
            insert_name(name_list)

        elif user_choice == "D":
            print_break()
            print("\nThis option will allow you to delete a name from the list.")
            name = input("\nEnter the name you want to delete: ")
            delete_name(name, name_list)

        elif user_choice == "F":
            print_break()
            print("\nThis option will allow you to search for a name in the list.")
            name = input("\nWhat name would you like to check for in the list? ")
            if find_name(name, name_list):
                print(f"\n{name.capitalize()} is already in the list.")
            else:
                print(f"\n{name} is not in the list.")

        elif user_choice == "S":
            try:
                name_list.sort()
            except TypeError:
                print("\nThe data contained in your list isn't able to be sorted.")
            else:
                print("\nYour list has been sorted.")



        elif user_choice == "V":
            print_break()
            print("\nThis is a numbered display of the names currently stored in your list:\n\n")
            view_list(name_list)

        else: 
            print("\n=====     Invalid Selection!     =====")

menu()

## Testing
# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_7 (master)
# $ python MW19_L7_Copeland.py

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: r

# =========================================


# This option will read a file into a list for you.

# Please enter the file name: peeple

# =====     Error!     =====

# The following error occurred: [Errno 2] No such file or directory: 'peeple.txt'

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: r

# =========================================


# This option will read a file into a list for you.

# Please enter the file name: people.txt

# Your file was successfully read.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: v

# =========================================


# This is a numbered display of the names currently stored in your list:


# 1) Lu, 2) Joe, 3) Luis, 4) Zelda, 5) Chad, 6) Nguyen, 7) Mindy, 8) Anne, 9) Lee, 10) George,

# 11) Max, 12) Antoine, 13) Terry, 14) Maria, 15) An, 16) Victor, 17) Larry, 18) Steve, 19) Anita, 20) Joline,

# 21) Charles,
# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: s

# Your list has been sorted.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: v

# =========================================


# This is a numbered display of the names currently stored in your list:


# 1) An, 2) Anita, 3) Anne, 4) Antoine, 5) Chad, 6) Charles, 7) George, 8) Joe, 9) Joline, 10) Larry,

# 11) Lee, 12) Lu, 13) Luis, 14) Maria, 15) Max, 16) Mindy, 17) Nguyen, 18) Steve, 19) Terry, 20) Victor,

# 21) Zelda,
# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: f

# =========================================


# This option will allow you to search for a name in the list.

# What name would you like to check for in the list? max

# Max is already in the list.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: f

# =========================================


# This option will allow you to search for a name in the list.

# What name would you like to check for in the list? john

# john is not in the list.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: i

# =========================================


# This option will allow you to insert a name into the list.

# What name would you like to insert in the list? john

# At what position number would you like to insert the name? 5

# John has been inserted at position 5

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: v

# =========================================


# This is a numbered display of the names currently stored in your list:


# 1) An, 2) Anita, 3) Anne, 4) Antoine, 5) John, 6) Chad, 7) Charles, 8) George, 9) Joe, 10) Joline,

# 11) Larry, 12) Lee, 13) Lu, 14) Luis, 15) Maria, 16) Max, 17) Mindy, 18) Nguyen, 19) Steve, 20) Terry,

# 21) Victor, 22) Zelda,
# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: i

# =========================================


# This option will allow you to insert a name into the list.

# What name would you like to insert in the list? max

# Max is already in the list

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: i

# =========================================


# This option will allow you to insert a name into the list.

# What name would you like to insert in the list? robby

# At what position number would you like to insert the name? 25

# Robby has been inserted at the end of the list.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: v

# =========================================


# This is a numbered display of the names currently stored in your list:


# 1) An, 2) Anita, 3) Anne, 4) Antoine, 5) John, 6) Chad, 7) Charles, 8) George, 9) Joe, 10) Joline,

# 11) Larry, 12) Lee, 13) Lu, 14) Luis, 15) Maria, 16) Max, 17) Mindy, 18) Nguyen, 19) Steve, 20) Terry,

# 21) Victor, 22) Zelda, 23) Robby,
# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: s

# Your list has been sorted.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: v

# =========================================


# This is a numbered display of the names currently stored in your list:


# 1) An, 2) Anita, 3) Anne, 4) Antoine, 5) Chad, 6) Charles, 7) George, 8) Joe, 9) John, 10) Joline,

# 11) Larry, 12) Lee, 13) Lu, 14) Luis, 15) Maria, 16) Max, 17) Mindy, 18) Nguyen, 19) Robby, 20) Steve,

# 21) Terry, 22) Victor, 23) Zelda,
# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: d

# =========================================


# This option will allow you to delete a name from the list.

# Enter the name you want to delete: mary

# Mary is not in the list.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: d

# =========================================


# This option will allow you to delete a name from the list.

# Enter the name you want to delete: maria

# Maria was deleted from the list.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: v

# =========================================


# This is a numbered display of the names currently stored in your list:


# 1) An, 2) Anita, 3) Anne, 4) Antoine, 5) Chad, 6) Charles, 7) George, 8) Joe, 9) John, 10) Joline,

# 11) Larry, 12) Lee, 13) Lu, 14) Luis, 15) Max, 16) Mindy, 17) Nguyen, 18) Robby, 19) Steve, 20) Terry,

# 21) Victor, 22) Zelda,
# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: w

# =========================================


# This option will write your current list into a new file for you.
# You must enter a file name to write to.

# Please enter the file name: people_sorted

# Your file was successfully written.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: r

# =========================================


# This option will read a file into a list for you.

# Please enter the file name: people_sorted

# Your file was successfully read.

# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: v

# =========================================


# This is a numbered display of the names currently stored in your list:


# 1) An, 2) Anita, 3) Anne, 4) Antoine, 5) Chad, 6) Charles, 7) George, 8) Joe, 9) John, 10) Joline,

# 11) Larry, 12) Lee, 13) Lu, 14) Luis, 15) Max, 16) Mindy, 17) Nguyen, 18) Robby, 19) Steve, 20) Terry,

# 21) Victor, 22) Zelda,
# =========================================

# Please choose what you'd like to perform:

# R) Read File
# W) Write to File
# I) Insert in File
# D) Delete from File
# F) Find in File
# S) Sort a File
# V) View Contents of File
# Q) Quit

# Your choice: q

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_7 (master)
# $
