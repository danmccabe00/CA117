#!/usr/bin/env python

import sys

f = int(sys.argv[1]) + 1

def replace_with_X(m):
   if m % 3 == 0:
      return "X"
   else:
      return m

def primes(n):
   if n == 1:
      return False
   else:
      a = 2
      while n > a:
         if n % a == 0:
            return False
         a = a + 1
      return True


def main():
   print("Multiples of 3: " + "{}".format([n for n in range(1, f) if n % 3 == 0]))
   print("Multiples of 3 squared: " + "{}".format([n * n for n in range(1, f) if (n % 3 == 0)]))
   print("Multiples of 4 doubled: " + "{}".format([n * 2 for n in range(1, f) if (n % 4 == 0)]))
   print("Multiples of 3 or 4: " + "{}".format([n for n in range(1, f) if n % 3 == 0 or n % 4 == 0]))
   print("Multiples of 3 and 4: " + "{}".format([n for n in range(1, f) if n % 3 == 0 and n % 4 == 0]))
   print("Multiples of 3 replaced: " + "{}".format([replace_with_X(n) for n in range(1, f)]))
   print("Primes: " + "{}".format([n for n in range(1, f) if primes(n)]))

if __name__ == '__main__':
   main()
