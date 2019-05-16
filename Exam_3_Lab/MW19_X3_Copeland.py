##  Name:  T. Emerson Copeland
##  COSC 1336   MW19  Spell-Checker

def notice(exam_number, name):
    return f'\nSpell checking program by {name} for Exam {exam_number} lab.'

def load_dictionary(wordlist):

    try:
        infile = open('dictionary.txt', 'r')

        for line in infile:
            line = line.rstrip()
            wordlist.append(line)
            
    except:
        print('\n===   Sorry, the dictionary file was not loaded correctly!   ===')
        return False
    
    else:
        infile.close()
        print(f'\nThe dictionary contains {len(wordlist)} words')
        return True

def main():
    print(notice(3,'T. Emerson Copeland'))
    dictionary = []
    if load_dictionary(dictionary):
        spellcheck(dictionary)
    print('\nGoodbye!')

def spellcheck(dictionary):

    ## Function to remove any non-alpha characters from the beginning and end of a word
    def checkalpha(word):
        while True:
            if not word[0].isalpha():
                word = word.lstrip(word[0])
                            
            elif not word[-1].isalpha():
                word = word.rstrip(word[-1])
            else:
                break
        return word


    while True:

        user_file = input('\nEnter the name of the file to spell check (.txt optional, enter nothing to quit): ')

        if user_file == '':
            break
        else:
            if not user_file.endswith('.txt'):
                user_file += '.txt'
            
            try:
                infile = open(user_file,'r')

                wordcount = 0
                number_misspelled = 0

                for index,line in enumerate(infile,1):
                    linelist = line.split()
                    for word in linelist:
                        wordcount += 1
                        word = checkalpha(word)
                        if not word.lower() in dictionary:
                            print(f'\n{word} on line {index} not found')
                            number_misspelled += 1
                        
            except:
                print(f"\n===   Sorry, I couldn't find {user_file}   ===")
            else:
                print(f'\n{number_misspelled} of {wordcount} words not found in file: {user_file}')
                infile.close()
            
main()

## Test Output:

# $ python MW19_X3_Copeland.py

# Spell checking program by T. Emerson Copeland for Exam 3 lab.

# The dictionary contains 80372 words

# Enter the name of the file to spell check (.txt optional, enter nothing to quit): ::\/$!~

# ===   Sorry, I couldn't find ::\/$!~.txt   ===

# Enter the name of the file to spell check (.txt optional, enter nothing to quit): junk

# ===   Sorry, I couldn't find junk.txt   ===

# Enter the name of the file to spell check (.txt optional, enter nothing to quit): letter.txt

# Selena on line 2 not found

# horss on line 5 not found

# ranned on line 6 not found

# furr-way on line 6 not found

# werds on line 7 not found

# Plinkerton on line 11 not found

# 6 of 49 words not found in file: letter.txt

# Enter the name of the file to spell check (.txt optional, enter nothing to quit):

# Goodbye!

# hpd15@LAPTOP-P4P9TKIA MINGW64 ~/Desktop/ACC Classes/Spring 2019/fundamentals_of_programming_1/Exam_3_Lab (master)
# $ 
