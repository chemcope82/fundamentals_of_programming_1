# Name: T. Emerson Copeland     MW19
# COSC1336  Lab 6

def print_break():
    print("\n=========================================\n")


# Part 1
def is_a_prime(num):
    isPrime = True
    i=2

    while (i<num):
        if (num%i==0):
            isPrime = False
            return isPrime
        else:
            i+=1
    else:
        return isPrime

def make_1000_primes():

    count = 1

    num_to_check = 3

    outfile = open("MW19_L6_Copeland_1000Primes.txt", "w")

    outfile.write("{:<6}".format("2"))

    while (count < 1000):
        if is_a_prime(num_to_check):
            outfile.write("{:<6}".format(str(num_to_check)))
            count += 1

            if (count % 10 == 0):
                outfile.write("\n")

            num_to_check +=1
        
        else:
            num_to_check += 1
    
    outfile.close()
    print_break()
    print("Your list of prime numbers was saved to the file: \'MW19_L6_Copeland_1000Primes.txt\'")


# Part 2
def state_census():

    infile = open("StateCensus2010.txt", "r")

    total_population = 0
    texas_data = []
    max_state = []
    min_state = []
    
    while True:
        state_data = []

        for _ in range(3):
            line = infile.readline()
            line = line.rstrip("\n")

            if line == "":
                break
            
            state_data.append(line)
            
        if state_data == []:
            break
        
        state_data[2] = int(state_data[2])

        if total_population == 0:
            max_state = state_data
            min_state = state_data
        
        total_population += state_data[2]

        if state_data[2] < min_state[2]:
            min_state = state_data

        if state_data[2] > max_state[2]:
            max_state = state_data

        if state_data[0] == "Texas":
            texas_data = state_data

    print_break()
    print("\nAs of the 2010 Census Data:")
    print("\nThe total US population is {:,}.".format(total_population))
    print("\n{} has the greatest population with {:,} residents.".format(max_state[0], max_state[2]))
    print("\n{} is the least populated state with {:,} residents.".format(min_state[0], min_state[2]))
    print("\nThe average number of residents per state is {:,}.".format(total_population/50))
    print("\nThe population of Texas is {:,}".format(texas_data[2]))
    print_break()

    infile.close()


# Part 3
def sum_file(file_name):

    file_total = 0

    try:
        infile = open(file_name, "r")

        for line in infile:
            line = float(line)
            file_total += line

    except Exception as err:
        print(f"\n=====     Error!     =====\n\nThe following error occurred: {err}")
        return

    else:
        print_break()
        print("The sum of all data in {} is {:,}".format(file_name, file_total))
        print_break()
        infile.close()


def menu():

    while True:
        print_break()
        user_choice = input("Please choose what you'd like to perform:\n\n1) 1000 Primes\n2) State Census Data\n3) Sum of a File\nQ) Quit\n\nYour choice: ")
        
        if user_choice == "Q" or user_choice == "q":
            break
        elif user_choice == "1":
            make_1000_primes()
        elif user_choice == "2":
            state_census()
        elif user_choice == "3":
            file_name = input("\n\nPlease enter the name (including the file extension) of the file you'd like to open: ")
            sum_file(file_name)
        else: 
            print("\n=====     Invalid Selection!     =====")

menu()


## Test Output:
# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_6 (master)
# $ python MW19_L6_Copeland.py

# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: 1

# Your list of prime numbers was saved to the file: 'MW19_L6_Copeland_1000Primes.txt'

# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: q

# =====     Invalid Selection!     =====

# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: q

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_6 (master)
# $ python MW19_L6_Copeland.py

# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: 1

# =========================================

# Your list of prime numbers was saved to the file: 'MW19_L6_Copeland_1000Primes.txt'

# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: 2

# =========================================


# As of the 2010 Census Data:

# The total US population is 309,077,989.

# California has the greatest population with 37,341,989 residents.

# Wyoming is the least populated state with 568,300 residents.

# The average number of residents per state is 6,181,559.78.

# The population of Texas is 25,268,418

# =========================================


# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: 3


# Please enter the name (including the file extension) of the file you'd like to open: data1.txt

# =========================================

# The sum of all data in data1.txt is 6,600.66

# =========================================


# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: 3


# Please enter the name (including the file extension) of the file you'd like to open: data2.txt

# =====     Error!     =====

# The following error occurred: could not convert string to float: 'three hundred\n'

# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: 3


# Please enter the name (including the file extension) of the file you'd like to open: data3.txt

# =====     Error!     =====

# The following error occurred: [Errno 2] No such file or directory: 'data3.txt'

# =========================================

# Please choose what you'd like to perform:

# 1) 1000 Primes
# 2) State Census Data
# 3) Sum of a File
# Q) Quit

# Your choice: q

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_6 (master)
# $
