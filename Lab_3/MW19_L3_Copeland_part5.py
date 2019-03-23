def drive_car():
    print("\n ===================================== \n")

    battery_charged = True
    got_car = True
    drunk = False
    gas = 2  # (gallons) # gas currently in the tank of the car
    distance = 100 # miles from home
    mpg = 35 # miles per gallon expected to be used driving home
    nighttime = False
    headlights_out = True

    canDrive = True

    if not (got_car):
        canDrive = False
    elif (drunk):
        canDrive = False
    elif not (battery_charged):
        canDrive = False
    elif (gas*mpg < distance):
        canDrive = False
    elif (nighttime) and (headlights_out):
        canDrive = False

    if canDrive:
        print("You can drive home")
    else:
        print("Better not drive home")

