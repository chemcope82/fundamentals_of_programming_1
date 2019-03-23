# Name: T. Emerson Copeland     MW19
# COSC1336, Lab 3 Decision Structures

# Lab 3 Part 1:
def dress_for_weather():
    print("\n ===================================== \n")
    print("Go to the window and look outside. \n")
    temp = int(input("What is the temperature in degrees Fahrenheit?  "))
    if (temp <= 45):
        print("\nBrrr, that's cold. Better wear a coat!")
    print('\nOpen the door and look outside. \n')
    isRaining = input("Is it raining (y/n)?  ").upper() # cast input to upper case to avoid upper/lower confusion for testing the condition
    if (isRaining == "Y"):
        print("\nUh oh, better bring an umbrella.")
    print("\nTime to go outside.")
    print("\n ===================================== \n")

# Lab 3 Part 2:
def flowchart():
    print("\n ===================================== \n")
    lastMeal = int(input("How many hours has it been since you ate last?  \n"))
    isHungry = input("Are you hungry now (y/n)?  ").upper()
    if (isHungry == "Y"):
        if (lastMeal >= 3):
            print("\nLets get some food! \nAhh, that feels better!")
        else:
            print("\nIt hasn't been that long since you ate last...")
    else:
        print("\nYou need to exercise more then!")
    print("\nNow let's go play outside")
    print("\n ===================================== \n")

# Lab 3 Part 3:
def rps():
    print("\n ===================================== \n")
    print("Let's play a game of Rock, Paper, Scissors\n")
    Player1 = input("Player1 choose R)ock, P)aper, or S)cissors:  ").upper()
    Player2 = input("Player2 choose R)ock, P)aper, or S)cissors:  ").upper()

    # Default invalid input for either player to choose Rock
    if (Player1 != "R") and (Player1 != "S") and (Player1 != "P"):
        Player1 = "R"
    if (Player2 != "R") and (Player2 != "S") and (Player2 != "P"):
        Player2 = "R"

    # Logic for deciding who won the game:
    if (Player1 == "R"):
        if (Player2 == "R"):
            print ("Player 1 and Player2 tied (Both players chose Rock)")
        elif (Player2 == "P"):
            print ("Player 2 wins! (Paper beats Rock)")
        else:
            print ("Player 1 wins! (Rock beats Scissors)")
    elif (Player1 == "P"):
        if (Player2 == "P"):
            print ("Player 1 and Player2 tied (Both players chose Paper)")
        elif (Player2 == "S"):
            print ("Player 2 wins! (Scissors beats Paper)")
        else:
            print ("Player 1 wins! (Paper beats Rock)")
    else:
        if (Player2 == "S"):
            print ("Player 1 and Player2 tied (Both players chose Scissors)")
        elif (Player2 == "R"):
            print ("Player 2 wins! (Rock beats Scissors)")
        else:
            print ("Player 1 wins! (Scissors beats Paper)")
    print("\n ===================================== \n")


# Lab 3 Part 4:
def seasons():
    print("\n ===================================== \n")
    season = input("Choose a season:\n\nEnter 1 for Spring\nEnter 2 for Summer\nEnter 3 for Autumn\nEnter 4 for Winter\n\nYour choice is: ")

    if (season != "1") and (season != "2") and (season != "3") and (season != "4"):
        print("\nHey goober, you need to pick a number 1-4! ")
    elif (season == 1):
        print("\nSpring is usually rainy")
    elif (season == "2"):
        print("\nSummer is the hottest season")
    elif (season == "3"):
        print("\nAutumn is when the leaves change color")
    else:
        print("\nWinter is the coldest season")

# Lab 3 Part 5:
def drive_car():
    print("\n ===================================== \n")

    battery_charged = True
    got_car = True
    drunk = False
    gas = 2  # (gallons) # gas currently in the tank of the car
    distance = 100 # miles from home
    mpg = 35 # miles per gallon expected to be used driving home
    nighttime = False
    headlights_out = True

    canDrive = True

    if not (got_car):
        canDrive = False
    elif (drunk):
        canDrive = False
    elif not (battery_charged):
        canDrive = False
    elif (gas*mpg < distance):
        canDrive = False
    elif (nighttime) and (headlights_out):
        canDrive = False

    if canDrive:
        print("You can drive home")
    else:
        print("Better not drive home")

# Lab 3 Part 6:
def quit():
        print("\n ===================================== \n")
        print("Goodbye!")

# Using a while loop to collect user input for what part to run
while True:
    print("\n ===================================== \n")

    userChoice = input("Choose which part you want to perform\n\n\
        1) Dress for Weather\n\
        2) Flowchart\n\
        3) Rock, Paper, Scissors\n\
        4) Seasons\n\
        5) Drive Car\n\
        6) Quit Now\n\nEnter the Number of Your Choice: ")

    if userChoice == "1":
        dress_for_weather()
    elif userChoice == "2":
        flowchart()
    elif userChoice == "3":
        rps()
    elif userChoice == "4":
        seasons()
    elif userChoice == "5":
        drive_car()
    elif userChoice == "6":
        quit()
        break
    else:
        print("You need to enter a number 1-6")

## Test Cases

#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 1

#  =====================================

# Go to the window and look outside.

# What is the temperature in degrees Fahrenheit?  35

# Brrr, that's cold. Better wear a coat!

# Open the door and look outside.

# Is it raining (y/n)?  y

# Uh oh, better bring an umbrella.

# Time to go outside.

#  =====================================


#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice:1

#  =====================================

# Go to the window and look outside.

# What is the temperature in degrees Fahrenheit?  35

# Brrr, that's cold. Better wear a coat!

# Open the door and look outside.

# Is it raining (y/n)?  n

# Time to go outside.

#  =====================================


#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 1

#  =====================================

# Go to the window and look outside.

# What is the temperature in degrees Fahrenheit?  75

# Open the door and look outside.

# Is it raining (y/n)?  y

# Uh oh, better bring an umbrella.

# Time to go outside.

#  =====================================


#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 2

#  =====================================

# How many hours has it been since you ate last?
# 5
# Are you hungry now (y/n)?  n

# You need to exercise more then!

# Now let's go play outside

#  =====================================


#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 2

#  =====================================

# How many hours has it been since you ate last?
# 1
# Are you hungry now (y/n)?  y

# It hasn't been that long since you ate last...

# Now let's go play outside

#  =====================================


#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice:3

#  =====================================

# Let's play a game of Rock, Paper, Scissors

# Player1 choose R)ock, P)aper, or S)cissors:  r
# Player2 choose R)ock, P)aper, or S)cissors:  p
# Player 2 wins! (Paper beats Rock)

#  =====================================


#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 3

#  =====================================

# Let's play a game of Rock, Paper, Scissors

# Player1 choose R)ock, P)aper, or S)cissors:
# Player2 choose R)ock, P)aper, or S)cissors:  S
# Player 1 wins! (Rock beats Scissors)

#  =====================================


#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 4

#  =====================================

# Choose a season:

# Enter 1 for Spring
# Enter 2 for Summer
# Enter 3 for Autumn
# Enter 4 for Winter

# Your choice is: Spring

# Hey goober, you need to pick a number 1-4!

#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 4

#  =====================================

# Choose a season:

# Enter 1 for Spring
# Enter 2 for Summer
# Enter 3 for Autumn
# Enter 4 for Winter

# Your choice is: 2

# Summer is the hottest season

#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 5

#  =====================================

# Better not drive home

#  =====================================

# Choose which part you want to perform

#         1) Dress for Weather
#         2) Flowchart
#         3) Rock, Paper, Scissors
#         4) Seasons
#         5) Drive Car
#         6) Quit Now

# Enter the Number of Your Choice: 6

#  =====================================

# Goodbye!

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/CSC1336 Programming/Lab_3
# $