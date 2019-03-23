## Part 2

def is_a_number(num): #Created a function to check if user input is numeric
    
    try:
        float(num)
        isNumber = True
    except:
        isNumber = False
        
    return isNumber

print("\n==========================================================\n")
print("What size triangle would you like to draw?\n\
You can enter values between 1 and 20.\n\
Entering '0' will quit ")

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
                    for j in range(i+1):
                        print("*", end="")
                    print()
                print()
        else:
            print("\n====  You must choose a box size between 1 and 20!  ====")
    else:
        print("\n====  You must enter a number!  ====")