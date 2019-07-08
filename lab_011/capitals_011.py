#!/usr/bin/env python

import sys

def cap(x):
    if len(x) > 1:
        if len(x) > 2:
            return x[0].capitalize() + x[1:-1] + x[-1].capitalize()
        else:
            return x[0].capitalize() + x[-1].capitalize()

def main():
    for line in sys.stdin:
        capped = cap(line.strip())
        if capped:
           print(capped)

if __name__ == '__main__':
    main()
