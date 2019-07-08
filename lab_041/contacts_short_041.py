import sys

a = []
def contact(l, c):
      c = c.strip()
      if c in l:
         return ("Phone: " + l[c])
      else:
         return "No such contact"

def main():
   d = {}
   with open(sys.argv[1]) as f:
      for lines in f:
         (name, number) = lines.strip().split()
         d[name] = number
   for line in sys.stdin:
      print("Name: " + line.strip())
      print(contact(d, line))

if __name__ == '__main__':
   main()
