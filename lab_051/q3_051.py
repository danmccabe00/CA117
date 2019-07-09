import sys

def censor(l):
   for w in l:
      if w.islower():
         l = l.replace(w, "-")
   return l.strip()

def main():
   for lines in sys.stdin:
      list = censor(lines).split("-")
      print(max(list, key=len))

if __name__ == '__main__':
   main()
