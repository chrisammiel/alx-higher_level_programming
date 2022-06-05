#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = int(repr(number)[-1])
print('Last digit of {} is {}'.format(number, Last_digit))
