#!/usr/bin/env python

import sys
a = []
def pal(s):
  l = []
  for c in s:
   if c[-1].isalnum():
      l.append(c)
   else:
    l.append(c[:-1])
  for b in l:
   if b not in a:
      a.append(b)
  return len(a)

def main():
   tot = 0
   for line in sys.stdin:
      pal(line.lower().strip().split())
   print(len(a) - 1)

if __name__ == '__main__':
    main()
