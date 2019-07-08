#!/usr/bin/env python

import sys

def cam(s):
   i = 0
   while i < len(s):
      s[i] = s[i].capitalize()
      i = i + 1
   return " ".join(s)

def main():
    for line in sys.stdin:
        s = line.lower().strip().split()
        print(cam(s))

if __name__ == '__main__':
    main()
