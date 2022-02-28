import keyboard
import mouse
from time import sleep


# This program is for joke purposes and is not to be used to

#
def textSpam(time):
    i = 0
    if isinstance(time, int):
        for i in range(time):
            if i < 1:
                print('Program will begin in five seconds. please open program.')
                sleep(5.00)
            else:
                keyboard.write('hi')
                # sleep(3)
                # keyboard.send('backspace')
                # keyboard.send('backspace')
                # sleep(2)
    else:
        print('please enter a number.')
    keyboard.add_hotkey('left windows', quit(textSpam()))
def agreement():
    print("""This program is intended for joke purposes and 
    is not meant to be used for any trolling purposes""")
    agreementanswer = input("""Do you understand?  
0 for yes 1 for no: """)

    if agreementanswer == 0 or 1:
        repeat = input('How many times would you like this repeated?: ')
        repeat = int(repeat)

        textSpam(repeat)
    else:
        print('please follow instructions.')





