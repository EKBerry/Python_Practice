from typing import Any

import keyboard
import mouse
from time import sleep




def start_up():
    print(
        """This program is intended for joke purposes and is 
not meant to be used for any trolling purposes""")
    agreement_answer = input(
        """Do you understand?  
        1 for yes 
        0 for no: """)
    agreement_answer = int(agreement_answer)


    # 0 or 1 are the only acceptable answers. Then runs it through the main function
    if agreement_answer == 1:
        repeat = input('How many times would you like this repeated? (2-10 recommend): ')
        repeat = int(repeat)
        text_spam(repeat)

    # For now the programs will just end.
    elif agreement_answer == 0:
        print('Sorry.')
        exit()
    # This only happens if a letter or 3< is put in
    else:
        print('Sorry.')
        exit()
#initiates the hardcoded macro and returns an array.
def initiate_macro(base_macro):
    base_macro = [keyboard.write('hi'),
    sleep(1), keyboard.send('enter'),
    sleep(1), keyboard.write('How are you?'),
    sleep(1), keyboard.send('enter')]
    return base_macro

def text_spam(time):
    # Set variable to assign later.
    base = []

    for i in range(time+1):
        if i <= 0:
            print('5 seconds.')
            sleep(5.00)
        else:
            initiate_macro(base)
            i += 1

start_up()

