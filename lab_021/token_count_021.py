#!/usr/bin/env python

import sys

def pal(s):
   l = []
   for c in s:
      l.append(c)
   return len(l)

def main():
   tot = 0
   for line in sys.stdin:
      tot = tot + pal(line.lower().strip().split())
   print(tot)

if __name__ == '__main__':
   main()
