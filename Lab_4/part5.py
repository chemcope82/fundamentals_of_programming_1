## Part 5

def kaleidoscope():
    print("\n==========================================================\n")
    print("This will allow you to draw circles like a kaleidoscope\n")
    print("Enter '0' for the number of circles to quit\n")
    print("Click on the drawing screen after it's completed to exit.\n")

    def is_a_number(num): #Created a function to check if user input is numeric
        
        try:
            float(num)
            isNumber = True
        except:
            isNumber = False
            
        return isNumber


    while True:
        numCircles = input("\nEnter the number of circles you want to draw: ")
        if is_a_number(numCircles):
            numCircles = int(numCircles)
            break
        else:
            print("\n====  You must enter a number!  ====")

    while True:
        if (numCircles == 0):
            print("\n=====   Goodbye!   =====\n")
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
    t.screen.mainloop()

kaleidoscope()