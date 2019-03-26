# Name: T. Emerson Copeland     MW19
# COSC1336, Lab 5

import random

def print_break():
    print("\n=========================================\n")

## Intro to functions
def intro(): 
    print_break()
    
    def f1_greeting():    
        print("Greetings Earth People")

    def f2_hello(name):
        print(f"Hello {name}")

    def f3_sum(num1,num2):
        print(f"The sum of {num1} and {num2} is {num1 + num2}")

    def f4_average(num1,num2):
        return(f"The average of {num1} and {num2} is {(num1+num2)/2}")

    def f5_minmax(num1,num2):
        if(num1 > num2):
            return{"min":num2, "max":num1}
        else:
            return{"min":num1, "max":num2}

    def f6_myName():
        return("My name is T. Emerson Copeland")

    def f7_lastname_firstname():
        return{"Last": "Copeland", "First": "T. Emerson"}

    def f8_combine_hundreds(hun=3,ten=2,one=1):
        return(f"{hun}{ten}{one}")

    def f9_place():
        def city():
            print("Austin", end=", ")
        def state():
            print("TX")
        
        city()
        state()

    def f10_face():
        def eye():
            print("(o)", end="")
        def nose():
            print("<=>")
        def mouth():
            print("\\\\-----//")
        eye()
        print("       ", end="")
        eye()
        print("\n\n     ", end="")
        nose()
        print("\n  ", end="")
        mouth()

    f1_greeting()
    f2_hello("Emerson")
    f3_sum(4,6)
    print(f4_average(10,20))
    print(f5_minmax(5,10))
    print(f5_minmax(25,10))
    print(f6_myName())
    print(f7_lastname_firstname())
    print(f8_combine_hundreds())
    print(f8_combine_hundreds(9,8,2))
    f9_place()
    f10_face()

# For the remaining parts, 
def is_a_number(num):  
    """This is a simple boolean function to check if a variable is a number."""

    try:
        float(num)
        isNumber = True
    except:
        isNumber = False

    return isNumber

def launch(): # Part 1

    def fill_booster(num):
        print(f"Fill booster fuel tank {num}.")
        print("  open valve")
        print("  pre-freeze tank")
        print("  attach filler hose")
        print("  pressurize fuel supply")
        print("  fill tank")
        print("  secure and seal shutoff valve")

    def start_engine(num):
        print(f"Start engine {num}")
        print("  ignition sequence start")
        print("  start ignition spark generator")
        print("  open fuel valve")
        print("  verify ignition temperature")
        print("  stop ignition spark generator")
        print(f"  engine {num} is started")

    input("Press enter to begin the launch sequence...")

    print("This program launches a rocket.")
    print("start launch sequence")
    fill_booster(1)
    fill_booster(2)
    fill_booster(3)
    start_engine(1)
    start_engine(2)
    print("3, 2, 1, 0, BLASTOFF!!!")
    print("Thank you. Keep looking up!")


def tip_table(): # Part 2
    def display_total_due(bill_with_tax, tip_rate, tax_rate):
        bill_without_tax = bill_with_tax / (1 + tax_rate)
        tip = bill_without_tax * tip_rate
        total_due = bill_with_tax + tip
        print("Total due with {0: .0%} tip: ${1: .2f}".format(tip_rate,total_due))

    TAX_RATE = .0825

    while True:
        bill_with_tax = input("\nEnter your total bill with tax: $")

        if is_a_number(bill_with_tax):
            bill_with_tax = float(bill_with_tax)
            break
        else:
            print("\n===  You must enter a valid number!  ===")

    print_break()
    display_total_due(bill_with_tax, 0.10, TAX_RATE)
    display_total_due(bill_with_tax, 0.15, TAX_RATE)
    display_total_due(bill_with_tax, 0.20, TAX_RATE)
    display_total_due(bill_with_tax, 0.25, TAX_RATE)
    print_break()

def add_one(number):
    modified = number + 1
    print(f"  At the top of add one: number={number}, modified={modified}")
    times_ten(modified)

def times_ten(number):
    modified = number * 10
    print(f"    At the top of times ten: number={number}, modified={modified}")
    less_100(modified)

def less_100(number):
    modified = number - 100
    print(f"      At the top of less 100: number={number}, modified={modified}")

def scope(): # Part 3

    while True:
        number = input("\nPlease enter a number: ")
        
        if is_a_number(number):
            number = int(number)
            break
        else:
            print("\n===  You must enter a valid number!  ===")
    print(f"\nAt the top of scope: number={number}")
    add_one(number)
    print(f"\nAt the bottom of scope: number={number}\n")


def sort(): # Part 4

    ## Start of sorting function
    def sort_list(*args):
        """This is a bubble sort function where the numbers to be sorted are provided as an arbitrary length number of arguments and then cast to a list"""
        sort_list = list(args)

        def greater_than(num1, num2):
            if(num1 > num2):
                return True
            else:
                return False

        def swap(num1, num2):
            return(num2, num1)
        
        while True:
            
            isSorted=True
            
            for i in range(len(sort_list)-1):
                if(greater_than(sort_list[i],sort_list[i+1])):
                    sort_list[i],sort_list[i+1] = swap(sort_list[i], sort_list[i+1])
                    isSorted=False
                
            if isSorted:
                break
        
        return sort_list
    ## End of sorting function

    run_10_times = 0
    print_break()

    while (run_10_times < 10):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        num3 = random.randint(1,100)

        print(f"The random numbers [{num1}, {num2}, {num3}] sort to: {sort_list(num1,num2,num3)}\n")
        run_10_times += 1

    print_break()


def ACC(): # Part 5
    print_break()
    print("This function has not been completed")
    print_break()

def main():
    print('\nHello. This is cosc1336 lab 5 on functions.\n')
    while True:
        print_break()
        option =  input('Please choose from the following options:\n\n0) Intro\n1) Launch\n2) Tip Table\n3) Scope\n4) Sort\n5) ACC\n6) Quit\n\nYour choice: ')
        option=option.lower()
        if option == '0':
            intro()    
        elif option == '1':
            launch()
        elif option == '2':
            tip_table()
        elif option == '3':
            scope()
        elif option == '4':
            sort()
        elif option == '5':
            ACC()           
        elif option == '6' or option == 'q':
            break
        else:
            print('  Invalid option, please try again.')
    print('\nGoodbye')

main()    


# Test Output:

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_5 (master)
# $ python MW19_L5_Copeland.py

# Hello. This is cosc1336 lab 5 on functions.


# =========================================

# Please choose from the following options:

# 0) Intro
# 1) Launch
# 2) Tip Table
# 3) Scope
# 4) Sort
# 5) ACC
# 6) Quit

# Your choice: 0

# =========================================

# Greetings Earth People
# Hello Emerson
# The sum of 4 and 6 is 10
# The average of 10 and 20 is 15.0
# {'min': 5, 'max': 10}
# {'min': 10, 'max': 25}
# My name is T. Emerson Copeland
# {'Last': 'Copeland', 'First': 'T. Emerson'}
# 321
# 982
# Austin, TX
# (o)       (o)

#      <=>

#   \\-----//

# =========================================

# Please choose from the following options:

# 0) Intro
# 1) Launch
# 2) Tip Table
# 3) Scope
# 4) Sort
# 5) ACC
# 6) Quit

# Your choice: 1
# Press enter to begin the launch sequence...
# This program launches a rocket.
# start launch sequence
# Fill booster fuel tank 1.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Fill booster fuel tank 2.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Fill booster fuel tank 3.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Start engine 1
#   ignition sequence start
#   start ignition spark generator
#   open fuel valve
#   verify ignition temperature
#   stop ignition spark generator
#   engine 1 is started
# Start engine 2
#   ignition sequence start
#   start ignition spark generator
#   open fuel valve
#   verify ignition temperature
#   stop ignition spark generator
#   engine 2 is started
# 3, 2, 1, 0, BLASTOFF!!!
# Thank you. Keep looking up!

# =========================================

# Please choose from the following options:

# 0) Intro
# 1) Launch
# 2) Tip Table
# 3) Scope
# 4) Sort
# 5) ACC
# 6) Quit

# Your choice: 2

# Enter your total bill with tax: $10.82

# =========================================

# Total due with  10% tip: $ 11.82
# Total due with  15% tip: $ 12.32
# Total due with  20% tip: $ 12.82
# Total due with  25% tip: $ 13.32

# =========================================


# =========================================

# Please choose from the following options:

# 0) Intro
# 1) Launch
# 2) Tip Table
# 3) Scope
# 4) Sort
# 5) ACC
# 6) Quit

# Your choice: 3

# Please enter a number: 25

# At the top of scope: number=25
#   At the top of add one: number=25, modified=26
#     At the top of times ten: number=26, modified=260
#       At the top of less 100: number=260, modified=160

# At the bottom of scope: number=25


# =========================================

# Please choose from the following options:

# 0) Intro
# 1) Launch
# 2) Tip Table
# 3) Scope
# 4) Sort
# 5) ACC
# 6) Quit

# Your choice: 4

# =========================================

# The random numbers [3, 79, 53] sort to: [3, 53, 79]

# The random numbers [69, 31, 50] sort to: [31, 50, 69]

# The random numbers [72, 6, 77] sort to: [6, 72, 77]

# The random numbers [81, 79, 87] sort to: [79, 81, 87]

# The random numbers [71, 60, 90] sort to: [60, 71, 90]

# The random numbers [54, 71, 89] sort to: [54, 71, 89]

# The random numbers [89, 68, 17] sort to: [17, 68, 89]

# The random numbers [62, 81, 82] sort to: [62, 81, 82]

# The random numbers [53, 85, 63] sort to: [53, 63, 85]

# The random numbers [42, 66, 25] sort to: [25, 42, 66]


# =========================================


# =========================================

# Please choose from the following options:

# 0) Intro
# 1) Launch
# 2) Tip Table
# 3) Scope
# 4) Sort
# 5) ACC
# 6) Quit

# Your choice: 5

# =========================================

# This function has not been completed

# =========================================


# =========================================

# Please choose from the following options:

# 0) Intro
# 1) Launch
# 2) Tip Table
# 3) Scope
# 4) Sort
# 5) ACC
# 6) Quit

# Your choice: 6

# Goodbye

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_5 (master)
# $
