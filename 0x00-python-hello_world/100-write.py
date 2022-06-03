#!/usr/bin/python3 
import sys
f = open("chris2.txt", "a" )
f.write("\nand that piece of art is useful - Dora Korpar, 2015-10-19")
f.close()

f = open("chris2.txt", "r")
print(f.read())
sys.stderr.write("spam\n")
os.write(2, b"spam\n")