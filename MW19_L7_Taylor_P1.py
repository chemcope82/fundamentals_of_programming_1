# Name: Victoria Taylor
# COSC 1336, Lab 7, Instructions, Lists, Tuples

# Part 1: Sorting
# Define Function
def main():
    # create Boolean variable
    entered = False
    # get user's input
    file_entry = input('Enter the name of the file to be sorted: ')
    # create conditions for the Filename's input variant
    # use endswith to check entry ending for extension .txt
    if file_entry.endswith('.txt'):
        entered = True
    else:
        # append '.txt' if not entered by user
        file_entry += '.txt'
        # notify user that .txt has been added to file name
        print ('".txt" extension appended to filename entry.')
    # open read file
    file = open(file_entry, 'r')
    # create list
    name_list = list()
    # establish "line count" variable
    elements = 0
    # processing elements in list
    for line in file:
        elements += 1
        # removing white space and 'next line' characters to make list
        line = line.rstrip('\n')
        # adds each line to the end of the list
        name_list.append(line)
    # close file and sort list
    file.close()
    name_list.sort()
    # inform user that file was opened, lines counted, and sorted to list

    print(file_entry, 'has been opened.')
    print(elements, "lines were found, and sorted into a list")
    # stripping filename of ".txt" for ease of printing to user
    new_name = file_entry.rstrip('.txt')
    # modify file ending name for clarification
    new_name += '_sorted.txt'
    print('The sorted list below has been renamed:', new_name)
    # output list for user
    print(name_list)
    # writing file with new name
    outfile = open(new_name,'w')
    for i in range(0,len(name_list)):
        # formatting list
        outfile.write(name_list[i]+'\n')
    # close the file
    outfile.close()

    p2 = 'a'
    p2 = input('Enter choice: i)nsert a name, d)elete a name, f)ind a name: or enter to stop\n')
    while p2 != '':
        if p2 == 'i':
            name = input('What name to add: ')
            name_list = insertName(name_list, name)
            view(name_list)
        elif p2 == 'd':
            name = input('What name to delete: ')
            name_list = deleteName(name_list, name)
            view(name_list)
        elif p2 == 'f':
            name = input('What name to find: ')
            if findName(name_list,name):
                print(name,'was not found')
            else:
                print(name,'was found')
        p2 = input('Enter a choice: i)nsert a name, d)elete a name, f)ind a name: or press enter to stop\n')

    menuOption(mylist)

def insertName(name_list,name):
    if findName(name_list,name):
        name_list.append(name)
        name_list.sort()
    else:
        print('That name is all ready in the list')
    return name_list

def findName(name_list,name):
    flag = True
    for i in range(0,len(name_list)):
        if name_list[i] == name:
            flag = False
    return flag

def deleteName(name_list,name):
    for i in range(0,len(name_list)):
        if name_list[i] == name:
            del(name_list[i])
    return name_list

def view(name_list):
    for i in range(0,len(name_list)):
        print(name_list[i])

def menuOption(name_list):
    choice = input('Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, q)uit: ')
    while choice != '':
        if choice == 'r':
            file_entry = input('Enter file name.(enter nothing to quit): ')
            #write function
        elif choice == 'w':
            file_entry = input('Whar file to write output to.(enter nothing for people_out.txt): ')
            #write function
        elif choice == 'i':
            name = input('What name to add: ')
            name_list = insertName(name_list,name)
        elif choice == 'd':
            name = input('What name to delete: ')
            name_list = deleteName(name_list,name)
        elif choice == 'f':
            name = input('What name to find: ')
            if findName(name_list,name):
                print(name,'was found')
            else:
                print(name,'was not found')
        elif choice == 's':
            name_list.sort()
        elif choice == 'v':
            view(mylist)
        else:
            print('Thanks for playing')

        choice = input('Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, q)uit: ')

main()

