# Write Function that uses regEX to check if pass string is strong enough.
# Needs at least 8 characters long, contains both upper and lowercase, at least 1 digit.

import pyperclip, re

passRegex = re.compile(r'([a-zA-Z(0-9)+]{8,})')

def stronkPassCheck():
    password = input('Enter a stronk password: ')
    mo = passRegex.search(password)
    if mo == None:
        print('Please try another password.')
        return False
    else:
        print('Password Accepted')
        return True

stronkPassCheck()

#need to fix! length and characters are fine, needs at least 1 number!!!


