import sys

def sort_on_second(t):
   return t[1]

def build_dictionary(t):
   d = {}
   with open(t, "r") as f:
      line = f.readlines()
   for lines in line:
      words = lines.strip().split()
      d[" ".join(words[:-1])] = int(words[-1])
   return d

def main():
   res = {}
   a = build_dictionary(sys.argv[1])
   for lines in sys.stdin:
      tot = 0
      l = lines.strip().split(",")
      i = 1
      while i < len(l):
         if l[i] in a:
            tot = tot + a[l[i]]
         else:
            tot = tot + 100
         i = i + 1
      res[l[0]] = tot

   for k, v in sorted(res.items(), key=sort_on_second):
      maxkv = len(max(res.keys(), key=len))
      maxv = len(str(sorted(res.items(), key=sort_on_second, reverse=True)[0][1]))
      print("{:>{:d}s} : {:{:d}d}".format(k, maxkv, v, maxv))

if __name__ == '__main__':
   main()
