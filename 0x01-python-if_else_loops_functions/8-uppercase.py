#!/usr/bin/python3
def uppercase(str):
    for i in str[100]:
        if ord('a') <= ord(str) <= ord('z'):
            print("{}".format(str-32))
