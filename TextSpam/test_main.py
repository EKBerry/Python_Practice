from unittest import TestCase




class Test(TestCase):
    def test_text_spam(self):
        repeat = input('How many times would you like this repeated?: ')
        repeat = int(repeat)
        if isinstance(repeat,str):
            print()

    def test_text_spam(self):
        print("""This program is intended for joke purposes and 
        is not meant to be used for any trolling purposes""")
        agreementanswer = input("""Do you understand?  
    0 for yes 1 for no: """)

        if agreementanswer == 0 or 1:
            repeat = input('How many times would you like this repeated?: ')
            repeat = int(repeat)

            print(repeat)
        else:
            print('please follow instructions.')



