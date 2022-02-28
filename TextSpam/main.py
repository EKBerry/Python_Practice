from typing import Any

import keyboard
import mouse
from time import sleep


# Used to quickly set up the array to iterate through
# instead of having a long list to copy-paste
# Will style later
def initiate(base_macro):

         base_macro = [keyboard.write('hi'), sleep(1), keyboard.send('enter'), sleep(1), keyboard.write('How are you?'),
                       sleep(1), keyboard.send('enter')]
         return base_macro
# What starts the entire program. If you agree you
# get prompted and begin the text_spam.
def agreement():
    # Don't use this to be harmful.
    print(
        """This program is intended for joke purposes and is 
not meant to be used for any trolling purposes""")

    # Actual program starts here.
    agreement_answer = input(
        """Do you understand?  
        1 for yes 
        0 for no: """)
    # Making sure that the answer is an INT and not a letter
    agreement_answer = int(agreement_answer)
    #This is in case someone puts a letter inside the prompt.
    if agreement_answer == 0 or 1:
        if agreement_answer == 1:
            # 0 or 1 are the only acceptable answers
            repeat = input('How many times would you like this repeated? (2-10 recommend): ')
            repeat = int(repeat)
            # runs through the main program.
            text_spam(repeat)
        # For now the programs will just end.
        elif agreement_answer == 0:
            print('Sorry.')
            exit()

        else:
            print('no you do not.')
            exit()
    else:
        print('no you do not.')
        exit()
# def prompt():
#     number = input('Enter a number')
#     number = int(number)
#     textSpam(number)
def text_spam(time):
    i = 0
    base = []

    for i in range(time):
        if i <= 0:
            print('5 seconds.')
            sleep(5.00)
        else:
            initiate(base)
            i += 1


agreement()
# textSpam(3)
