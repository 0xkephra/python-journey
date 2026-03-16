# EXERCISE 2

Num = float(input('Pick a number : '))
if (Num % 2 == 0):
    print('The number you picked is even')
elif (Num % 4 == 0):
    print('The number you picked is a multiple of 4')
else:
    print('The number you picked is odd')

num = float(input('Pick a first number: '))
check = float(input('Pick a second number: '))
if num % check == 0:
    print('check divides evenly into num')
else:
    print('check did not divides evenly into num')
