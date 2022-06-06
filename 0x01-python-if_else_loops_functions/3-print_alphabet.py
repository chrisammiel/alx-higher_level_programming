#!/usr/bin/python3
alph = 97
for i in range(97, 122):
    if i == 101 and i == 112:
        continue
    print(chr(i), end="")
    alph += 1
