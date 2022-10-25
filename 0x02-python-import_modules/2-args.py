#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = len(sys.argv) - 1
    if j == 0:
        print("0 arguments.")
    elif j == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(j))
    for i in range(j):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
