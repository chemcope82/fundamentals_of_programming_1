import turtle
t = turtle.Turtle()

t.penup() # Beginning of Letter T
t.goto(-200,0)
t.setheading(90)
t.pendown()
t.forward(200)
t.penup()
t.goto(-300,200)
t.right(90)
t.pendown()
t.forward(200)
t.penup() # End of Letter T

t.goto(0,0) # Beginning of Letter E
t.left(90)
t.pendown()
t.forward(200)
t.right(90)
t.forward(100)
t.penup()
t.goto(0,0)
t.pendown()
t.forward(100)
t.penup()
t.goto(0,100)
t.pendown()
t.forward(100) 
t.penup() # End of Letter E

t.goto(300,200) # Beginning of Letter C
t.setheading(180)
t.pendown()
t.circle(100,180) # End of Letter C
