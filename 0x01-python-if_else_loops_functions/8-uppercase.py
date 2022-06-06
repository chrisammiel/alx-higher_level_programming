#!/usr/bin/python3
def uppercase(str):
    for i in str[100]:
        if ord('a') <= ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
            print("{}".format(i), end="")
