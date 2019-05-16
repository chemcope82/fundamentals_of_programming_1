# Name: T. Emerson Copeland     MW19
# COSC1336  Lab 7

def print_break():
    print("\n=========================================\n")

def get_filename():
    file_name = input("\nPlease enter the file name: ")
    
    if not file_name.endswith('.txt'):
        file_name = file_name + ".txt"
    
    return file_name

def read_file():
    some_list = []
    try:
        infile = open(get_filename(), 'r')
        for line in infile:
            line = line.rstrip("\n")
            some_list.append(line)
    
    except Exception as err:
        print(f"\n=====     Error!     =====\n\nThe following error occurred: {err}")
    else:
        infile.close()
        print("\nYour file was successfully read.")
        return some_list

def write_file(some_list):

    if len(some_list) <= 0:
        print("\nYour list is currently empty.")
    else:
        print("You must enter a file name to write to.")
        try:
            outfile = open(get_filename(), 'w')
            for item in some_list:
                outfile.write(item + "\n")
            
        except Exception as err:
            print(f"\n=====     Error!     =====\n\nThe following error occurred: {err}")

        else:
            outfile.close()
            print("\nYour file was successfully written.")

def view_list(some_list):
    if len(some_list) <= 0:
        print("\nYour list is currently empty.")
    else:
        for index, item in enumerate(some_list, 1):
            print(f"{item}, ", end="")
            if (index % 10 == 0):
                print("\n")

def sort_list(some_list):

    if len(some_list) <= 0:
        print("\nYour list is currently empty.")
    else:
        try:
            some_list.sort()
        except TypeError:
            print("\nThe data contained in your list isn't able to be sorted.")
        else:
            print("\nYour list has been sorted.")

def insert_name(some_list, name):
    if not find_name(some_list, name):
        some_list.append(name)

    return some_list

def find_name(some_list, target):
    return target in some_list

def delete_name(some_list, target):
    if find_name(some_list, target):
        del some_list[some_list.index(target)]
    
    return some_list

def main():

    name_list = []

    while True:
        print_break()
        user_choice = input("Please choose what you'd like to perform:\n\nR) Read File\nW) Write to File\n" \
        "I) Insert in File\nD) Delete from File\nF) Find in File" \
        "\nS) Sort a File\nV) View Contents of File\nQ) Quit\n\nYour choice: ")
        user_choice = user_choice.upper()

        if user_choice == "Q":
            print("\nGoodbye!")
            break

        elif user_choice == "R":
            print_break()
            print("\nThis option will read a file into a list for you.")
            name_list = read_file()

        elif user_choice == "W":
            print_break()
            print("\nThis option will write your current list into a new file for you.")
            write_file(name_list)

        elif user_choice == "I":
            print_break()
            print("\nThis option will allow you to insert a name into the list.")
            if len(name_list) <= 0:
                print("\nYour list is currently empty.")
            else:
                name = input("\nWhat name would you like to insert in the list? ")
                view_list(insert_name(name_list, name))

        elif user_choice == "D":
            print_break()
            print("\nThis option will allow you to delete a name from the list.")
            if len(name_list) <= 0:
                print("\nYour list is currently empty.")
            else:
                name = input("\nEnter the name you want to delete: ")
                view_list(delete_name(name_list, name))

        elif user_choice == "F":
            print_break()
            print("\nThis option will allow you to search for a name in the list.")
            if len(name_list) <= 0:
                print("\nYour list is currently empty.")
            else:
                name = input("\nWhat name would you like to check for in the list? ")
                print(find_name(name_list, name))

        elif user_choice == "S":
            sort_list(name_list)

        elif user_choice == "V":
            print_break()
            print("\nThis is a display of the names currently stored in your list:\n")
            view_list(name_list)

        else: 
            print("\n=====     Invalid Selection!     =====")

main()

