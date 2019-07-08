import sys
import string

def make_dictionary(f):
   d = {}
   for line in f:
      for w in line.strip().lower().split():
         w = w.strip(string.punctuation)
         for l in w:
            if not l:
               continue
            try:
               d[l] += 1
            except KeyError:
               d[l] = 1
   return d

def sort_on_second(t):
   return t[1]

def main():
   d = make_dictionary(sys.stdin)
   nd = {}
   for k in d:
      if k == "a" or k == "e" or k == "i" or k == "o" or k == "u":
         nd[k] = d[k]
   for k, v in sorted(nd.items(), key=sort_on_second, reverse=True):
      maxkv = len(max(nd.keys(), key=len))
      maxv = len(str(sorted(nd.items(), key=sort_on_second, reverse=True)[0][1]))
      print("{:>{:d}s} : {:{:d}d}".format(k, maxkv, v, maxv))

if __name__ == '__main__':
   main()
