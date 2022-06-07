#!/usr/bin/python3
if __name__ == "__main__":
    num_of_args = len(sys.argv[1:])
    i = 1
    while num_of_args >= 1:
        print("{}".format(0 + int(sys.argv[i])))
        i = i + 1
        