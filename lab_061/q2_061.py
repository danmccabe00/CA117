import sys

def main():
   for lines in sys.stdin:
      l = lines.strip().split()
      a = []
      i = 1
      while i < len(l) - 1:
         if int(l[i - 1]) < int(l[i]) and int(l[i + 1]) < int(l[i]):
            a.append(i)
         i = i + 1
      print(a)

if __name__ == '__main__':
   main()
