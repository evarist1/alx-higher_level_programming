#!/usr/bin/python3

import sys

def infinite_add(*args):
    result = sum(int(arg) for arg in args)
    print(result)

if __name__ == "__main__":
    # Get command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Call the function with the command-line arguments
    infinite_add(*arguments)
