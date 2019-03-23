## Part 1

def is_a_number(num): #Created a function to check if user input is numeric
    
    try:
        float(num)
        isNumber = True
    except:
        isNumber = False
        
    return isNumber

print("\n==========================================================\n")
print("What size box would you like to draw?\n\
You can enter values between 1 and 20.\n\
Entering '0' will quit ")

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
                        for column in range (boxSize):
                                print("*", end='')
                    else:
                        spaces = (boxSize-2)*" "
                        print(f"*{spaces}*", end="")
                    print()
            else:
                for row in range(boxSize):
                    for column in range(boxSize):
                        print("*", end='')
                    print()
        else:
            print("\n====  You must choose a box size between 1 and 20!  ====")
    else:
        print("\n====  You must enter a number!  ====")