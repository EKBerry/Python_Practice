from typing import Any

import keyboard
import mouse
from time import sleep


# Premade macro for quicker use and cleaner code
def initiate(base_macro):

    base_macro = [keyboard.write('hi'),
        sleep(1), keyboard.send('enter'),
        leep(1), keyboard.write('How are you?'),
        sleep(1), keyboard.send('enter')]
    return base_macro

def start_up():
    # Going to code this with regex later.
    agreement_answer = input(
        """
        Do not use this
        program to spam people
        Do you understand?  
        1 for yes 
        0 for no: """)

    agreement_answer = int(agreement_answer)
    if agreement_answer == 1:
        repeat = input('How many times would you like this repeated? (2-10 recommend): ')
        repeat = int(repeat)
        text_spam(repeat)

    elif agreement_answer == 0:
        print('Sorry.')
        exit()
    else:
        print('no you do not.')
        exit()


def text_spam(repeat):
    base = []

    for i in range(repeat+1):
        if i <= 0:
            print('5 seconds.')
            sleep(5.00)
        else:
            initiate(base)
            i += 1


start_up()

