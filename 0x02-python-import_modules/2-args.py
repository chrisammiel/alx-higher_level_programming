#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    if (len(sys.argv)-1) == 0:
        print("{} arguments.".format(len(sys.argv)-1))
    elif (len(sys.argv)-1) == 1:
        print("{} argument:".format(len(sys.argv)-1))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        l = len(argv)
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))

