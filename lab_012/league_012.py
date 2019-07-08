#!/usr/bin/env python

import sys

def main():
   big = 0
   a = []
   for line in sys.stdin:
      a.append(line.strip().split())
      j = 0
      while j < len(a):
         d = " ".join(a[j][1:-8])
         if big < len(d):
            big = len(d)
         j = j + 1
      n = "{:<" + str(big + 2) + "s}"
   print('{:>s}'.format("POS ") + n.format("CLUB") + "{:<4s}{:<4s}{:<4s}{:<3s}{:<4s}{:<4s}{:<3s}{:<3s}".format("P", "W", "D", "L", "GF", "GA", "GD", "PTS"))
   n = "{:<" + str(big + 1) + "s}"
   i = 0
   while i < len(a):
      p = " ".join(a[i][1:-8])
      print('{:>3s}'.format(a[i][0]) + " " + n.format(p) + "{:<2s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4}{:>4s}".format(a[i][-8], a[i][-7], a[i][-6], a[i][-5], a[i][-4], a[i][-3], a[i][-2], a[i][-1]))
      i = i + 1

if __name__ == '__main__':
   main()
