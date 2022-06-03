#!/usr/bin/python3
f = open("chris2.txt", "a" )
f.write("\nand that piece of art is useful - Dora Korpar, 2015-10-19")
f.close()

f = open("chris2.txt", "r")
print(f.read())