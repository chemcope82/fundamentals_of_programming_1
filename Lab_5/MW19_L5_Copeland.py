# Name: T. Emerson Copeland     MW19
# COSC1336, Lab 5, startup structure for menu-driven loop

import random

def print_break():
    print("\n=========================================\n")

def intro(): 
    def f1_greeting():    
        print("Greetings Earth People")

    def f2_hello(name):
        print(f"Hello {name}")

    def f3_sum(num1,num2):
        print(f"The sum of {num1} and {num2} is {num1 + num2}")

    def f4_average(num1,num2):
        return(f"The average is {(num1+num2)/2}")

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

def launch(): # Part 1. Get startup code from launch.py (provided)

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


def tip_table(): # Part 2. Get startup code from tip_table.py (provided)
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

def scope(): # Part 3. Get startup code from scope.py (provided)

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


def sort(): # Part 4. No startup code provided. See instructions.

    ## Start of sorting function
    def sort_list(*args):
        """This is a bubble sort function where numbers are provided as an arbitrary length number of arguments and then cast to a list to be sorted"""
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


def ACC(): # Part 5. Extra Credit: no startup code provided. See instructions.
    pass

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

# Test all options in one, last test run, and paste your output below:

