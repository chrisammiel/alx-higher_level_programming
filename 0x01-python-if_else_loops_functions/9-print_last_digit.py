#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        return int(repr((number)[-1:]) * -1)
    else:
        return int(repr(number)[-1:])
