## Name: T. Emerson Copeland
## MW19   COSC1336   Lab 10  Classes

class Clock():

    def __init__(self, hour=0, minute=0, second=0):
        if type(hour) == int and type(minute) == int and type(second) == int:
            if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
                self.__hour = hour
                self.__minute = minute
                self.__second = second
            else:
                print('\n===   Invalid Data, time is set to 0:00:00   ===')
                self.__hour = 0
                self.__minute = 0
                self.__second = 0
        else:
            print('\n===   Invalid Data, time is set to 0:00:00   ===')
            self.__hour = 0
            self.__minute = 0
            self.__second = 0
    
    def set_hour(self, hour):
        if type(hour) == int:
            if 0 <= hour <= 23:
                self.__hour = hour
        else:
            print('\n====    Invalid Hour    ====')
    
    def set_minute(self, minute):
        if type(minute) == int:
            if 0 <= minute <= 59:
                self.__minute = minute
        else:
            print('\n====    Invalid Minute    ====')

    
    def set_second(self, second):
        if type(second) == int:
            if 0 <= second <= 59:
                self.__second = second
        else:
            print('\n====    Invalid Second    ====')

    def get_hour(self):
        return self.__hour
    
    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second
    
    def __str__(self):
        am_pm = ''
        hour = None

        if self.__hour < 12:
            am_pm = 'AM'
            hour = self.__hour
        else:
            am_pm = 'PM'
            hour = self.__hour - 12

        return f'{hour}:{self.__minute:0>2}:{self.__second:0>2} {am_pm}'


# 1st instance of a Clock and testing
print('\n\n\n===   1st instance   ===\n')
my_watch = Clock(18,25,30)
print(my_watch)
my_watch.set_hour(22)
my_watch.set_minute(30)
my_watch.set_second(45)
print(my_watch)

# 2nd instance of a Clock and testing
print('\n\n\n===   2nd instance   ===\n')
grandfather_clock = Clock(12.5, 30, 30)
print(grandfather_clock)
grandfather_clock.set_hour('twelve')
grandfather_clock.set_minute(35)
print(grandfather_clock)

# 3rd instance of a Clock and testing
print('\n\n\n===   3rd instance   ===\n')
wall_clock = Clock(10, 100, 35)
print(wall_clock)
wall_clock.set_hour(5)
wall_clock.set_minute(5)
wall_clock.set_second(1)
print(wall_clock)

## Test Output:
# $ python MW19_L10_Copeland.py



# ===   1st instance   ===

# 6:25:30 PM
# 10:30:45 PM



# ===   2nd instance   ===


# ===   Invalid Data, time is set to 0:00:00   ===
# 0:00:00 AM

# ====    Invalid Hour    ====
# 0:35:00 AM



# ===   3rd instance   ===


# ===   Invalid Data, time is set to 0:00:00   ===
# 0:00:00 AM
# 5:05:01 AM

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Lab_10 (master)
# $ ^C
