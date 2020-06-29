# Chapter 2: Playing With the Import Module

import random
for i in range(0, 5, 2):
    print(i)
    print(random.randint(1, 90))
print()

from random import *
for i in range(3):
    print(randint(1, 99))
print()


import sys
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('This will not print')