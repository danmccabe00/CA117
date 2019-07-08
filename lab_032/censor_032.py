import sys

a = []
def censor(l, c):
   for w in l:
      if w in c:
         c = c.replace(w, len(w) * "@")
   return c.strip()

def main():
   with open(sys.argv[1]) as f:
      for lines in f:
         a.append(lines.strip())
   for line in sys.stdin:
      print(censor(a, line))

if __name__ == '__main__':
   main()
