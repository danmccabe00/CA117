#!/usr/bin/env python

import sys

def sub (x):
	y = x.split()
	return y[0] in (y[1])

def main():
    for line in sys.stdin:
        subbed = sub(line.lower().strip())
        print(subbed)

if __name__ == '__main__':
    main()
