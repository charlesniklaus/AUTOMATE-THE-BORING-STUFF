# Chapter 2 - Flow Control

name = ''
while True:
    print('Enter your name.')
    name = input()
    if name != 'Charles':
        continue
    elif name == 'Charles':
        print('Hi ' + name + '!')
        print('Enter your age')
        age = input()
        if age == '23':
            print('It is really you ' + name + '!')
            break
        else:
            print('You are not ' + name + '.')
print('You are welcome!')

