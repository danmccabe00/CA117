 #!/usr/bin/env python
 
import sys

def pas(s):
   tot = 0
   a = []
   for c in s:
      if c.isdigit():
         a.append("dig")
      if c.islower():
         a.append("low")
      if c.isupper():
         a.append("up")
      if c != " ":
         if not c.isalnum():
            a.append("oth")
   a.pop(len(a) - 1)
   if "dig" in a:
      tot = tot + 1
   if "low" in a:
      tot = tot + 1
   if "up" in a:
      tot = tot + 1
   if "oth" in a:
      tot = tot + 1
   return tot

def main():
   for line in sys.stdin:
         print(pas(line))

if __name__ == '__main__':
   main()
