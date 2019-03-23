## Part 4

def is_a_number(num): #Created a function to check if user input is numeric
    
    try:
        float(num)
        isNumber = True
    except:
        isNumber = False
        
    return isNumber

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

print("\n==========================================================\n")
print("Test to see if a number is prime.  Enter '0' to quit\n")

while True:
    num = input("\nEnter a positive integer to see if it is a prime number: ")
    if (num == '0'):
        break

    if is_a_number(num):
        num = int(num)

        if is_a_prime(num):
            print(f"\n{num} is a prime number!")
        else:
            print(f"\n{num} is a composite number.")
    else:
        print("\n====  You must enter a number!  ====")