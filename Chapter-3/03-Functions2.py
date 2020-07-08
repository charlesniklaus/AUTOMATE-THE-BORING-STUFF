# Chapter 3 - Exercise 2 (Input Validation)

def collatz(number):
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
        number = 3 * number + 1
    print(number)
    return number

num = input("Type in a number to run against the Collatz sequence: ")

try:
    num = int(num)
    while num != 1:
        num = collatz(num)

except ValueError:
    print("You did not type in a number")