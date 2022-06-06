#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = int(repr(number)[-1])
if number < 0:
    Last_digit = Last_digit * -1
    print('Last digit of {} is {} and is less than 6 and not 0 '.format(number, Last_digit)
else:
    if Last_digit > 5:
        print('Last digit of {} is {-} and is greater than 5'.format(number, Last_digit))
    elif Last_digit == 0:
        print('Last digit of {} is {} and is 0'.format(number, Last_digit))
    elif 6 > Last_digit != 0:
        print('Last digit of {} is {} and is less than 6 and not 0 '.format(number, Last_digit))
