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
