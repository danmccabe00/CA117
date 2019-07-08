#!/usr/bin/env python

import sys

def namm(s):
   for c in s[0]:
      if c == "." or c.isdigit():
         s[0] = s[0].replace(c, " ", 1)
      f = s[0].split()  
   return f[0].capitalize() + " " + f[1].capitalize()

def main():
    for line in sys.stdin:
        s = line.lower().strip().split("@")
        print(namm(s))

if __name__ == '__main__':
    main()
