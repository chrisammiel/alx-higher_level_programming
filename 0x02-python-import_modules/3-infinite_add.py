#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sm = 0
    for i in range(1, len(sys.argv)):
        sm = sm + int(sys.argv[i])
    print("{}".format(sm))
