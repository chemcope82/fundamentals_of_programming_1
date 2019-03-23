##  Name:  T. Emerson Copeland
##  COSC 1336   MW19 

print("\n================================================================\n")
print("This program computes the enrollment capacity for an ACC Campus")
print("\n================================================================\n")

def is_a_number(num):  ## Function to check if user input is numeric
    try:
        float(num)
        isNumber = True
    except:
        isNumber = False

    return isNumber

def calculate_capacity():

    max_capacity = 0

    while True:
        print("\n================================================================\n")

        campus = input("Please enter a campus abbreviation or 'Q' to quit: ").upper()

        if(campus == "Q"):
            if max_capacity != 0:
                max_capacity = format(max_capacity, ",")
                print(f"\nThe maximum capacity for all campuses entered is {max_capacity} students.")
            print("\n=====   Goodbye!   =====\n")
            return False
        elif(campus == "NRG") or (campus == "CYP") or (campus == "RRC"):
            while True:
                buildings = input("\nHow many buildings are on this campus? ")
                if is_a_number(buildings):
                    buildings = int(buildings)
                    break
                else:
                    print("\n=====   You must enter a number!   =====")
                    continue
            while True:
                classrooms = input("\nHow many classrooms are there per building? ")
                if is_a_number(classrooms):
                    classrooms = int(classrooms)
                    break
                else:
                    print("\n=====   You must enter a number!   =====")
                    continue
            while True:
                seats = input("\nHow many seats are there per classroom? ")
                if is_a_number(seats):
                    seats = int(seats)
                    break
                else:
                    print("\n=====   You must enter a number!   =====")
                    continue  
            capacity = buildings * classrooms * seats

            max_capacity += capacity

            capacity = format(capacity, ",")
            print(f"\nACC's {campus} campus can serve up to {capacity} students\n")
            continue
        else:
            print("\nYou must enter a valid campus code\n")

def print_help():
    print("\n================================================================\n")
    print("\nTo calculate campus capacity, this program will ask you to enter a campus, the number of buildings, number of classrooms, and number of seats.")
    print("\nValid campus inputs are 'NRG', 'CYP', and 'RRC'")
    print("\nYou need to enter numeric values for the buildings, classrooms, and seats")
    print("\nEnter 'Q' at the campus selection menu to quit")
    print("\n================================================================\n")

is_running = True

while is_running:
    menu_choice = input("Please choose from the following:\n\n( C )  Calculate capacity\n( H )  Help\n( Q )  Quit\n\nYour choice: " ).upper()
    if (menu_choice == 'C'):
        is_running = calculate_capacity()
    elif (menu_choice == 'H'):
        print_help()
    elif (menu_choice == 'Q'):
        print("\n=====   Goodbye!   =====\n")
        break
    else:
        print("\n=====   Invalid Choice!   =====\n")


## Test Data:

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/CSC1336 Programming/Exam_1_Lab
# $ python MW19_X1_Copeland.py

# ================================================================

# This program computes the enrollment capacity for an ACC Campus

# ================================================================

# Please choose from the following:

# ( C )  Calculate capacity
# ( H )  Help
# ( Q )  Quit

# Your choice: h

# ================================================================


# To calculate campus capacity, this program will ask you to enter a campus, the number of buildings, number of classrooms, and number of seats.

# Valid campus inputs are 'NRG', 'CYP', and 'RRC'

# You need to enter numeric values for the buildings, classrooms, and seats

# Enter 'Q' at the campus selection menu to quit

# ================================================================

# Please choose from the following:

# ( C )  Calculate capacity
# ( H )  Help
# ( Q )  Quit

# Your choice: c

# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: nrg

# How many buildings are on this campus? 4

# How many classrooms are there per building? 14

# How many seats are there per classroom? 24

# ACC's NRG campus can serve up to 1,344 students


# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: cyp

# How many buildings are on this campus? 5

# How many classrooms are there per building? 15

# How many seats are there per classroom? 25

# ACC's CYP campus can serve up to 1,875 students


# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: acc

# You must enter a valid campus code


# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: rrc

# How many buildings are on this campus? 6

# How many classrooms are there per building? 16

# How many seats are there per classroom? 26

# ACC's RRC campus can serve up to 2,496 students


# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: q

# The maximum capacity for all campuses entered is 5,715 students.

# =====   Goodbye!   =====


# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/CSC1336 Programming/Exam_1_Lab
# $

## Invalid Input Cases:

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/CSC1336 Programming/Exam_1_Lab
# $ python MW19_X1_Copeland.py

# ================================================================

# This program computes the enrollment capacity for an ACC Campus

# ================================================================

# Please choose from the following:

# ( C )  Calculate capacity
# ( H )  Help
# ( Q )  Quit

# Your choice: 1

# =====   Invalid Choice!   =====

# Please choose from the following:

# ( C )  Calculate capacity
# ( H )  Help
# ( Q )  Quit

# Your choice: c

# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: acc

# You must enter a valid campus code


# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: nrg

# How many buildings are on this campus? twelve

# =====   You must enter a number!   =====

# How many buildings are on this campus? 12

# How many classrooms are there per building? five

# =====   You must enter a number!   =====

# How many classrooms are there per building? 5

# How many seats are there per classroom? twenty

# =====   You must enter a number!   =====

# How many seats are there per classroom? 20

# ACC's NRG campus can serve up to 1,200 students


# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: quit

# You must enter a valid campus code


# ================================================================

# Please enter a campus abbreviation or 'Q' to quit: q

# The maximum capacity for all campuses entered is 1,200 students.

# =====   Goodbye!   =====


# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/CSC1336 Programming/Exam_1_Lab
# $
