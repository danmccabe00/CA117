#!/usr/bin/env python

import sys

def mid(x):
        if len(x) % 2 != 0:
            return x[len(x) // 2]
        else:
            return "No middle character!"

def main():
    for line in sys.stdin:
        midded = mid(line.strip())
        if midded:
           print(midded)

if __name__ == '__main__':
    main()
