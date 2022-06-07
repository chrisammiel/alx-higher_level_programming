#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    from calculator_1.py import add, sub, div, mul
    a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    if len(sys.args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
