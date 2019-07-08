 #!/usr/bin/env python
 
import sys

def plur(s):
    if s[-2:] == "ch" or s[-2:] == "sh" or s[-1] == "x" or s[-1] == "s" or s[-1] == "z" or s[-1] == "o":
      return s + "es"
    elif s[-1] == "f":
      return s[:-1] + "ves"
    elif s[-2:] == "fe":
      return s[:-2] + "ves"
    elif (s[-1] == "y") and s[-2] != "a" and s[-2] != "e" and s[-2] != "i" and s[-2] != "o" and s[-2] != "u":
      return s[:-1] + "ies"
    else:
      return s + "s"

def main():
   for line in sys.stdin:
      print(plur(line.strip()))

if __name__ == '__main__':
   main()
