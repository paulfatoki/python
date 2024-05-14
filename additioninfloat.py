# while loop guessing your password in an input
addition = 30.5 + 40.7
password=""

while addition != password:
    print('please enter the right addition')
    password = float(input())

print('Yes, the correct addition is ' + str (password) + '. You may enter.')