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