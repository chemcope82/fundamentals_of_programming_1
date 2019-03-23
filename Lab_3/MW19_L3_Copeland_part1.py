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
