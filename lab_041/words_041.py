import sys
import string

def make_dictionary(f):
   d = {}
   for line in f:
      for w in line.strip().lower().split():
         w = w.strip(string.punctuation)
         if not w:
            continue
         try:
            d[w] += 1
         except KeyError:
            d[w] = 1
   return d

def main():
   d = make_dictionary(sys.stdin)
   for k, v in sorted(d.items()):
      print("{:s} : {:d}".format(k, v))

if __name__ == '__main__':
   main()
