# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
# stored in spam, and prints Greetings! if anything else is stored in spam.
for spam in range(0, 4):
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings!')
print()


# Write a short program that prints the numbers 1 to 10 using a for loop.
# Then write an equivalent program that prints the numbers 1 to 10 using
# a while loop.
for i in range(1, 11):
    print(i)
print()

num = 1
while num < 11:
    print(num)
    num = num + 1
print()


# How will you Round up the float 5.5221
x = round(5.5221)
print(x)
print()


# How will you return the Absolute value of 22
y = abs(-22.7)
print(y)

# If you had a function named bacon() inside a module named spam, how
# would you call it after importing spam?
from spam import bacon