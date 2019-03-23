## Name: T. Emerson Copeland  MW19
## COSC1336, Lab 4: Repetition Structures


#Created a function to check if user input is numeric
def is_a_number(num): 
    try:
        float(num)
        isNumber = True
    except:
        isNumber = False

    return isNumber


## Lab 4 Part 1:
def drawBoxes():
    print("\n==========================================================\n")
    print("What size box would you like to draw?\n")
    print("You can enter values between 1 and 20.\n")
    print("Entering '0' will quit ")

    while True:
        boxSize = input("\nEnter the size of your box to draw: ")
        
        if boxSize == '0':
            break

        if is_a_number(boxSize):
            boxSize = int(boxSize)
            if (boxSize > 0) and (boxSize <= 20):
                print("\n")

                if (boxSize%2 != 0) and (boxSize != 1):
                    for row in range(boxSize):
                        if (row == 0) or (row == (boxSize-1)):
                            for _ in range (boxSize):
                                    print("*", end='')
                        else:
                            spaces = (boxSize-2)*" "
                            print(f"*{spaces}*", end="")
                        print()
                else:
                    for row in range(boxSize):
                        for _ in range(boxSize):
                            print("*", end='')
                        print()
            else:
                print("\n====  You must choose a box size between 1 and 20!  ====")
        else:
            print("\n====  You must enter a number!  ====")

## Lab 4 Part 2:
def drawTriangles():
    print("\n==========================================================\n")
    print("What size triangle would you like to draw?\n")
    print("You can enter values between 1 and 20.\n")
    print("Entering '0' will quit ")

    while True:
        triangleSize = input("\nEnter the size of your triangle to draw: ")
        
        if triangleSize == '0':
            break

        if is_a_number(triangleSize):
            triangleSize = int(triangleSize)
            if (triangleSize > 0) and (triangleSize <= 20):
                print("\n")
                for h in range(triangleSize):
                    for i in range(h+1):
                        for _ in range(i+1):
                            print("*", end="")
                        print()
                    print()
            else:
                print("\n====  You must choose a box size between 1 and 20!  ====")
        else:
            print("\n====  You must enter a number!  ====")

## Lab 4 Part 3:
def averageTemp():
    print("\n==========================================================\n")
    print("I'll help you calculate the average for a list of temperatures you provide.\n")
    print("You can enter temperatures between -5 and 115 Fahrenheit\n")
    print("Enter 'Q' at any time to quit entering temperaturess and find the average.")

    tempList = []  #Creating an empty list to hold temperature inputs
    freezingTemps = 0

    #Collecting input for temperatures
    while True:
        new_temp = input("\nEnter a temperature: ")
        if new_temp.upper() == 'Q':
            if len(tempList) == 0:
                print("\nYou didn't enter any data")
                return
            print("\n==========================================================\n")
            print(f"\nYou entered {len(tempList)} temperatures")
            print(f"\nThe highest temperature was {max(tempList)} degrees")
            print(f"\nThe lowest temperature was {min(tempList)} degrees")
            print(f"\nThe average temperature was {sum(tempList)/len(tempList)} degrees")
            print(f"\nThe number of freezing temperatures was {freezingTemps}")
            break
        if is_a_number(new_temp):
            new_temp = int(new_temp)
            if (new_temp) >= -5 and (new_temp <= 115):
                tempList.append(new_temp)
                if(new_temp <= 32):
                    freezingTemps =+1
            else:
                print("\n====  That's not within the allowed range of numbers!  ====")
        else:
            print("\n====  You must enter a number!  ====")


## Lab 4 Part 4:
def primeNumber():
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

    print("\n==========================================================\n")
    print("Test to see if a number is prime.  Enter '0' to quit\n")

    while True:
        num = input("\nEnter a positive integer to see if it is a prime number: ")
        if (num == '0'):
            break

        if is_a_number(num):
            num = int(num)

            if is_a_prime(num):
                print(f"\n{num} is a prime number!")
            else:
                print(f"\n{num} is a composite number.")
        else:
            print("\n====  You must enter a number!  ====")

## Lab 4 Part 5:
def kaleidoscope():
    print("\n==========================================================\n")
    print("This will allow you to draw circles like a kaleidoscope\n")
    print("Enter '0' for the number of circles to quit\n")
    print("Click on the drawing screen after it's completed to exit.\n")

    while True:
        numCircles = input("\nEnter the number of circles you want to draw: ")
        if is_a_number(numCircles):
            numCircles = int(numCircles)
            break
        else:
            print("\n====  You must enter a number!  ====")

    while True:
        if (numCircles == 0):
            return
        circleSize = input("\nEnter the size of the circles to draw: ")
        if is_a_number(circleSize):
            circleSize = int(circleSize)
            break
        else:
            print("\n====  You must enter a number!  ====")

    headingIncrement = (360 / numCircles)
    heading = 0
    circleCounter = 0

    import turtle
    t = turtle.Turtle()
    while (circleCounter < numCircles):
        t.setheading(heading)
        t.circle(circleSize)
        circleCounter += 1
        heading += headingIncrement

    t.screen.exitonclick()
    # this function will only run on the first attempt.  
    # After entering the two inputs on subsequent attempts, the turtle graphic fails to initialize and the entire program crashes

# Lab 4 Part 6:
def quit():
        print("\n=====   Goodbye!   =====\n")


## Using a while loop to collect user input for what part to run
while True:
    print("\n ===================================== \n")

    userChoice = input("Choose which part you want to perform\n\n\
        1) Draw Boxes\n\
        2) Draw Triangles\n\
        3) Average Temperature\n\
        4) Prime Numbers\n\
        5) Kaleidoscope\n\
        6) Quit Now\n\nEnter the Number of Your Choice: ")

    if userChoice == "1":
        drawBoxes()
    elif userChoice == "2":
        drawTriangles()
    elif userChoice == "3":
        averageTemp()
    elif userChoice == "4":
        primeNumber()
    elif userChoice == "5":
        kaleidoscope()
    elif userChoice == "6":
        quit()
        break
    else:
        print("You need to enter a number 1-6")


## Test Data:

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/CSC1336 Programming/Lab_4
# $ python MW19_L4_Copeland_parts1-6.py

#  =====================================

# Choose which part you want to perform

#         1) Draw Boxes
#         2) Draw Triangles
#         3) Average Temperature
#         4) Prime Numbers
#         5) Kaleidoscope
#         6) Quit Now

# Enter the Number of Your Choice: 1

# ==========================================================

# What size box would you like to draw?

# You can enter values between 1 and 20.

# Entering '0' will quit

# Enter the size of your box to draw: 5


# *****
# *   *
# *   *
# *   *
# *****

# Enter the size of your box to draw: 4


# ****
# ****
# ****
# ****

# Enter the size of your box to draw: 3


# ***
# * *
# ***

# Enter the size of your box to draw: 2


# **
# **

# Enter the size of your box to draw: 0

#  =====================================

# Choose which part you want to perform

#         1) Draw Boxes
#         2) Draw Triangles
#         3) Average Temperature
#         4) Prime Numbers
#         5) Kaleidoscope
#         6) Quit Now

# Enter the Number of Your Choice: 2

# ==========================================================

# What size triangle would you like to draw?

# You can enter values between 1 and 20.

# Entering '0' will quit

# Enter the size of your triangle to draw: 3


# *

# *
# **

# *
# **
# ***


# Enter the size of your triangle to draw: 4


# *

# *
# **

# *
# **
# ***

# *
# **
# ***
# ****


# Enter the size of your triangle to draw: 5


# *

# *
# **

# *
# **
# ***

# *
# **
# ***
# ****

# *
# **
# ***
# ****
# *****


# Enter the size of your triangle to draw: 0

#  =====================================

# Choose which part you want to perform

#         1) Draw Boxes
#         2) Draw Triangles
#         3) Average Temperature
#         4) Prime Numbers
#         5) Kaleidoscope
#         6) Quit Now

# Enter the Number of Your Choice: 3

# ==========================================================

# I'll help you calculate the average for a list of temperatures you provide.

# You can enter temperatures between -5 and 115 Fahrenheit

# Enter 'Q' at any time to quit entering temperaturess and find the average.

# Enter a temperature: 12

# Enter a temperature: 45

# Enter a temperature: 78

# Enter a temperature: 123

# ====  That's not within the allowed range of numbers!  ====

# Enter a temperature: 456

# ====  That's not within the allowed range of numbers!  ====

# Enter a temperature: -4

# Enter a temperature: 0

# Enter a temperature: 99

# Enter a temperature: q

# ==========================================================


# You entered 6 temperatures

# The highest temperature was 99 degrees

# The lowest temperature was -4 degrees

# The average temperature was 38.333333333333336 degrees

# The number of freezing temperatures was 1

#  =====================================

# Choose which part you want to perform

#         1) Draw Boxes
#         2) Draw Triangles
#         3) Average Temperature
#         4) Prime Numbers
#         5) Kaleidoscope
#         6) Quit Now

# Enter the Number of Your Choice: 25
# You need to enter a number 1-6

#  =====================================

# Choose which part you want to perform

#         1) Draw Boxes
#         2) Draw Triangles
#         3) Average Temperature
#         4) Prime Numbers
#         5) Kaleidoscope
#         6) Quit Now

# Enter the Number of Your Choice: 4

# ==========================================================

# Test to see if a number is prime.  Enter '0' to quit


# Enter a positive integer to see if it is a prime number: 25

# 25 is a composite number.

# Enter a positive integer to see if it is a prime number: 17

# 17 is a prime number!

# Enter a positive integer to see if it is a prime number: 9008711

# 9008711 is a composite number.

# Enter a positive integer to see if it is a prime number: 0

#  =====================================

# Choose which part you want to perform

#         1) Draw Boxes
#         2) Draw Triangles
#         3) Average Temperature
#         4) Prime Numbers
#         5) Kaleidoscope
#         6) Quit Now

# Enter the Number of Your Choice: 5

# ==========================================================

# This will allow you to draw circles like a kaleidoscope

# Enter '0' for the number of circles to quit

# Click on the drawing screen after it's completed to exit.


# Enter the number of circles you want to draw: 8

# Enter the size of the circles to draw: 75

#  =====================================

# Choose which part you want to perform

#         1) Draw Boxes
#         2) Draw Triangles
#         3) Average Temperature
#         4) Prime Numbers
#         5) Kaleidoscope
#         6) Quit Now

# Enter the Number of Your Choice: 6

# =====   Goodbye!   =====


# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/CSC1336 Programming/Lab_4
# $

