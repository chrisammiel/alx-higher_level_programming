#!/usr/bin/python3
def uppercase(str):
    for i in str[100]:
        if ord('a') <= ord(i) <= ord('z'):
            print("{}".format(i-32), end="")
