#!/usr/bin/env python

import sys

def contains(chars, s):
  if len(chars) == len(s):
   for c in chars:
      if c in s:
         s = s.replace(c, "", 1)
      else:
        return False
   return True
  return False

def main():
    for line in sys.stdin:
        [chars, s] = line.lower().strip().split()
        print(contains(chars, s))

if __name__ == '__main__':
    main()
