#!/usr/bin/env python

import sys

def pal(s):
   l = []
   for c in s:
      if c.isalnum():
         l.append(c)
   return l == l[::-1]

def main():
   for line in sys.stdin:
      print(pal(line.lower()))

if __name__ == '__main__':
   main()
