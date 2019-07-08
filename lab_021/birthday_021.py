#!/usr/bin/env python

import sys
import calendar

def days(y, m, d):
   b = calendar.weekday(y, m, d)
   if b == 0:
      return "You were born on a Monday and Monday's child is fair of face."
   elif b == 1:
      return "You were born on a Tuesday and Tuesday's child is full of grace."
   elif b == 2:
      return "You were born on a Wednesday and Wednesday's child is full of woe."
   elif b == 3:
      return "You were born on a Thursday and Thursday's child has far to go."
   elif b == 4:
      return "You were born on a Friday and Friday's child is loving and giving."
   elif b == 5:
      return "You were born on a Saturday and Saturday's child works hard for a living."
   elif b == 6:
      return "You were born on a Sunday and Sunday's child is fair and wise and good in every way."


def main():
   day = int(sys.argv[1])
   month = int(sys.argv[2])
   year = int(sys.argv[3])
   print(days(year, month, day))

if __name__ == '__main__':
   main()
