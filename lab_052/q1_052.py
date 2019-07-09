import sys

def main():
   l = []
   s = sys.argv[1]
   n = int(sys.argv[2])
   for c in s:
      l.append(c)
   i = 0
   while i < n:
      l.insert(0, l[len(l) - 1])
      l.pop(len(l) - 1)
      i = i + 1
   a = "".join(l)
   print(a)

if __name__ == '__main__':
   main()
