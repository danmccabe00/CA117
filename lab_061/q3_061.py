import sys

def count(l):
   dig = 0
   big = 0
   small = 0
   other = 0
   for c in l:
      if c.isdigit():
         dig = 1
      elif c.islower():
         small = 1
      elif c.isupper():
         big = 1
      elif not c.isalnum():
         other = 1
   tot = dig + big + small + other
   return tot

def main():
   for lines in sys.stdin:
      ls = []
      for letters in lines.strip():
         ls.append(letters)
      print(count(ls))

if __name__ == '__main__':
   main()
