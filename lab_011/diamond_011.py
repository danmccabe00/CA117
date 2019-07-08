#!/usr/bin/env python

import sys

def main():
    n = int(sys.argv[1])
    i = 1
    while i <= n:
       print((" " * (n - i)) + ("* " * (i - 1)) + ("*"))
       i = i + 1
    i = i - 2
    while 0 < i:
       print((" " * (n - i)) + ("* " * (i - 1) + ("*")))
       i = i - 1

if __name__ == '__main__':
    main()
