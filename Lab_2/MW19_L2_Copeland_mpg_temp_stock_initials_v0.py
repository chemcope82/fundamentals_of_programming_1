# Name: T. Emerson Copeland     MW19
# COSC1336, Lab 2, 4 parts:
#   part 1: Compute MPG
#   part 2: Convert temperature
#   part 3: Stock sale
#   part 4: Draw initials using turtle graphics
#
# Part 1: Compute the mileage for a car.
#   Ask the user for all values.
#   Format mileage amounts to appear like: xx.x
#   Run at least two test cases.

print("Lab 2: Part 1: compute MPG;     Part 2: convert temp;")
print("       Part 3: stock gain/loss; Part 4: draw initials.\n")

print("This part computes gas mileage.")
# Ask for and get the vehicle make and model. These are separate items.
# Ask for and get the amount of miles traveled.
# Ask for and get the number of gallons used.
# Calculate the gas mileage.
# Output the results.
# Include: vehicle make and model, miles traveled, gallons used, mileage.
vehicleMake = input("What is the make of your vehicle? ")
vehicleModel = input("What is the model of your vehicle? ")
miles = float(input("How many miles were driven? "))
gallons = float(input("How many gallons of fuel were used? "))
print("\n======================================================\n")
print("You drove your", vehicleMake, vehicleModel, miles, "miles and used", gallons, "gallons of fuel.")
print("Your fuel economy was " + format(miles / gallons, ".1f" )+ " MPG")
print("Drive safely.\n")


# Part 2: Convert temperature units from celsius to fahrenheit
#   Ask the user for all values.
#   Format temperature amounts to appear like: xx.x
#   Run at least two test cases.
print("This part performs a temperature unit conversion from celsius to fahrenheit.")
# Ask for and get celsius temperature
# Convert celsius temperature to fahrenheit
# Display result
tempInCelcius = float(input("What is the temperature in degrees Celcius? "))
print("\n======================================================\n")
print("The temperature is", format((9/5)*tempInCelcius + 32, ".1f"), "degrees Fahrenheit.")
print("Enjoy the great outdoors.\n")


# Part 3: Compute gain (or loss) on security transaction
#   Ask the user for all values (see textbook)
#   Perform stock transaction, buy and sell, show profit/loss
#   Format dollar amounts to appear like: $1,234.56
#   Run test case with this data:
#     buy 2000 shares at $40 per share, commission is 3%
#     sell 2000 shares at $42.75, commission is 3%
print ("This part computes the result of a stock transaction.")
# put your new code here
stocksBought = int(input("How many shares did you buy? "))
priceBought = float(input("What was the buying price per share? "))
commissionBought = float(input("What percent commission was paid for the purchase? (Enter just a number, ie enter 2.5 for a 2.5% commission) "))
stocksSold = int(input("How many shares were sold? "))
priceSold = float(input("What was the selling price per share? "))
commissionSold = float(input("What percent commission was paid for the sale? (Enter just a number, ie enter 2.5 for a 2.5% commission) "))
purchasePrice = (stocksBought * priceBought)
commissionPaidBuy = purchasePrice * (commissionBought/100)
sellProfit = (stocksSold * priceSold)
commissionPaidSell = sellProfit * (commissionSold/100)
netProfit = (sellProfit - commissionPaidSell) - (purchasePrice + commissionPaidBuy)
print("\n======================================================\n")
print("You paid $" + format(purchasePrice, ".2f") + " to buy the stocks.")
print("You paid $" + format(commissionPaidBuy, ".2f") + " in commission to buy.")
print("You made $" + format(sellProfit, ".2f") + " when you sold the stocks.")
print("You paid $" + format(commissionPaidSell, ".2f") + " in commission to sell.")
if (netProfit > 0):
  print("You made $" + format(netProfit, ".2f") + " from this stock transaction.")
elif (netProfit == 0):
  print("You broke even from this stock transaction.")
else:
  print("You lost $" + format(netProfit*-1, ".2f") + " from this stock transaction.")
print ("Buy high, sell higher, make money, spend wisely.\n")


if False: # Change False to True when ready to work on Part 4
  # Part 4: Write initials on screen using Python Turtle graphics
  #
  # Using python turtle graphics, draw initials on the screen
  # My initials are 'PT' <change this to your initials>
  #
  # Provided: Startup code that draws instructor's initials
  # Modify this startup code to draw your initials:
  #   Two letters is enough. Draw just one if it is taking too long.
  #   Use straight lines and circles
  #   Use penup to position pen, pendown to start drawing
  #   Subdivide each portion into "paragraphs"
  #   Drawing should complete within 5 seconds
  #   Drawing should be inside a box of 400 x 400 pixels
  #   Comment what you are doing

  print("This part draws my initials.")
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

  t.penup()
  t.goto(0,-200)
  t.write('   TEC is for T. Emerson Copeland, Good-bye!')
  t.hideturtle()    # hide turtle to see initials clearly 

  print("End of turtle lab to draw my initials.")



# Paste your output for parts 1, 2, and 3 below:

# Part 1:

  # Test Case 1:
  # What is the make of your vehicle? Toyota
  # What is the model of your vehicle? 4Runner
  # How many miles were driven? 100
  # How many gallons of fuel were used? 5

  # ======================================================

  # You drove your Toyota 4Runner 100.0 miles and used 5.0 gallons of fuel.
  # Your fuel economy was 20.0 MPG
  # Drive safely.

  # Test Case 2:
  # What is the make of your vehicle? Honda
  # What is the model of your vehicle? Element
  # How many miles were driven? 250
  # How many gallons of fuel were used? 9.7

  # ======================================================

  # You drove your Honda Element 250.0 miles and used 9.7 gallons of fuel.
  # Your fuel economy was 25.8 MPG
  # Drive safely.

  # Test Case 3:
  # What is the make of your vehicle? Ford
  # What is the model of your vehicle? F-350
  # How many miles were driven? 55
  # How many gallons of fuel were used? 5.5

  # ======================================================

  # You drove your Ford F-350 55.0 miles and used 5.5 gallons of fuel.
  # Your fuel economy was 10.0 MPG
  # Drive safely.

# Part 2:

  # Test Case 1:
  # What is the temperature in degrees Celcius? 25

  # ======================================================

  # The temperature is 77.0 degrees Fahrenheit.
  # Enjoy the great outdoors.

  # Test Case 2:
  # What is the temperature in degrees Celcius? 12.275

  # ======================================================

  # The temperature is 54.1 degrees Fahrenheit.
  # Enjoy the great outdoors.

  # Test Case 3:
  # What is the temperature in degrees Celcius? -22.35

  # ======================================================

  # The temperature is -8.2 degrees Fahrenheit.
  # Enjoy the great outdoors.

# Part 3:

# Test Case 1:
  # How many shares did you buy? 2000
  # What was the buying price per share? 40
  # What percent commission was paid for the purchase? (Enter just a number, ie enter 2.5 for a 2.5% commission) 3
  # How many shares were sold? 2000
  # What was the selling price per share? 42.75
  # What percent commission was paid for the sale? (Enter just a number, ie enter 2.5 for a 2.5% commission) 3

  # ======================================================

  # You paid $80000.00 to buy the stocks.
  # You paid $2400.00 in commission to buy.
  # You made $85500.00 when you sold the stocks.
  # You paid $2565.00 in commission to sell.
  # You made $535.00 from this stock transaction.
  # Buy high, sell higher, make money, spend wisely.

  # Test Case 2:

  # How many shares did you buy? 1000
  # What was the buying price per share? 25
  # What percent commission was paid for the purchase? (Enter just a number, ie enter 2.5 for a 2.5% commission) 4
  # How many shares were sold? 1000
  # What was the selling price per share? 23.50
  # What percent commission was paid for the sale? (Enter just a number, ie enter 2.5 for a 2.5% commission) 4

  # ======================================================

  # You paid $25000.00 to buy the stocks.
  # You paid $1000.00 in commission to buy.
  # You made $23500.00 when you sold the stocks.
  # You paid $940.00 in commission to sell.
  # You lost $3440.00 from this stock transaction.
  # Buy high, sell higher, make money, spend wisely.

  #Test Case 3:

  #How many shares did you buy? 1000
  # What was the buying price per share? 25
  # What percent commission was paid for the purchase? (Enter just a number, ie enter 2.5 for a 2.5% commission) 0
  # How many shares were sold? 1000
  # What was the selling price per share? 25
  # What percent commission was paid for the sale? (Enter just a number, ie enter 2.5 for a 2.5% commission) 0

  # ======================================================

  # You paid $25000.00 to buy the stocks.
  # You paid $0.00 in commission to buy.
  # You made $25000.00 when you sold the stocks.
  # You paid $0.00 in commission to sell.
  # You broke even from this stock transaction.
  # Buy high, sell higher, make money, spend wisely.
