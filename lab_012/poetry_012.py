#!/usr/bin/env python

import sys

a = []
def main():
   big = 0
   for line in sys.stdin:
      if big < len(line):
         big = len(line)
      a.append(line.strip())
   n = "{:^" + str(big - 1) + "s}"
   for t in a:
      print(n.format(t))

if __name__ == '__main__':
    main()
