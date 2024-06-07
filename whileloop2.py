# while loop guessing your password in an input
passcode ='food'
password=""

while passcode != password:
    print('your password is wrong, please enter the right  password?')
    password = input()

print('Yes, the password is ' + password + '. You may enter.')