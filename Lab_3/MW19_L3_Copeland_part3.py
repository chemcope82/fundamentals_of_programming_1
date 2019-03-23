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
