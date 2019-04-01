# Name: T. Emerson Copeland     MW19
# COSC1336  Lab 6

def print_break():
    print("\n=========================================\n")


# Part 1
def is_a_prime(num):
    isPrime = True
    i=2

    while (i<num):
        if (num%i==0):
            isPrime = False
            return isPrime
        else:
            i+=1
    else:
        return isPrime

def make_1000_primes():

    count = 1

    num_to_check = 3

    outfile = open("MW19_L6_Copeland_1000Primes.txt", "w")

    outfile.write("{:<6}".format("2"))

    while (count < 1000):
        if is_a_prime(num_to_check):
            outfile.write("{:<6}".format(str(num_to_check)))
            count += 1

            if (count % 10 == 0):
                outfile.write("\n")

            num_to_check +=1
        
        else:
            num_to_check += 1
    
    outfile.close()

def state_census():

    infile = open("StateCensus2010.txt", "r")

    total_population = 0
    texas_data = []
    max_state = []
    min_state = []
    
    while True:
        state_data = []

        for _ in range(3):
            line = infile.readline()
            line = line.rstrip("\n")

            if line == "":
                break
            
            state_data.append(line)
            
        if state_data == []:
            break
        
        state_data[2] = int(state_data[2])

        if total_population == 0:
            max_state = state_data
            min_state = state_data
        
        total_population += state_data[2]

        if state_data[2] < min_state[2]:
            min_state = state_data

        if state_data[2] > max_state[2]:
            max_state = state_data

        if state_data[0] == "Texas":
            texas_data = state_data

    print_break()
    print("\nAs of the 2010 Census Data:")
    print("\nThe total US population is {:,}.".format(total_population))
    print("\n{} has the greatest population with {:,} residents.".format(max_state[0], max_state[2]))
    print("\n{} is the least populated state with {:,} residents.".format(min_state[0], min_state[2]))
    print("\nThe average number of residents per state is {:,}.".format(total_population/50))
    print("\nThe population of Texas is {:,}".format(texas_data[2]))
    print_break()

    infile.close()

