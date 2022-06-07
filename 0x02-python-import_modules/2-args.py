#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)-1) == 1:
        print("{} argument:".format(len(sys.argv)-1))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
    num_of_args = len(sys.argv[1:])
    i = 1
    while num_of_args >= 1:
        print("{}: {}".format(i, argv[i]))
        i += 1
