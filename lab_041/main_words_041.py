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
   nd = {}
   for k in d:
      if 2 < d[k] and 3 < len(k):
         nd[k] = d[k]
   for k, v in sorted(nd.items()):
      maxkv = len(max(nd.keys(), key=len))
      print("{:>{:d}s} : {:{:d}d}".format(k, maxkv, v, 2))

if __name__ == '__main__':
   main()
