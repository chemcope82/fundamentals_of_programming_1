## Part 3

tempList = []  #Creating an empty list to hold temperature inputs
def is_a_number(num): #Created a function to check if user input is numeric
    
    try:
        float(num)
        isNumber = True
    except:
        isNumber = False
        
    return isNumber


print("\n==========================================================\n")
print("I'll help you calculate the average for a list of temperatures you provide.\n\
You can enter temperatures between -5 and 115 Fahrenheit\n\
Enter 'Q' at any time to quit entering temperaturess and find the average.")

#Collecting input for temperatures
while True:
    new_temp = input("\nEnter a temperature: ")
    if new_temp.upper() == 'Q':
        break

    if is_a_number(new_temp):
        if (int(new_temp)) >= -5 and (int(new_temp) <= 115):
            tempList.append(int(new_temp))
        else:
            print("\n====  That's not within the allowed range of numbers!  ====")
    else:
        print("\n====  You must enter a number!  ====")

print("\nThe average temperature is", sum(tempList)/len(tempList), "degrees")