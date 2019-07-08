#!/usr/bin/env python

import sys

def conv(n, m):
   tot = 0
   i = 0
   while i < len(n):
      new = int(n[i]) * (int(m) ** (len(n) - 1 - i ))
      tot = tot + new
      i = i + 1
   return tot

def main():
    for line in sys.stdin:
        [n, m] = line.lower().strip().split()
        print(conv(n, m))

if __name__ == '__main__':
    main()
