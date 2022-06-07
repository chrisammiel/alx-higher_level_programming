#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)-1) == 0:
        print("{} argument.".format(len(sys.argv)-1))
    elif (len(sys.argv)-1) == 1:
        print("{} argument:".format(len(sys.argv)-1))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
    num_of_args = len(sys.argv[1:])
    i = 1
    while num_of_args >= 1:
        print(f'{i}: {sys.argv[i]}')
        i = i + 1
