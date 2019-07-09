import sys

def main():
   l = list(sys.argv[1])
   i = 1
   while i < len(l):
      l[i], l[i - 1] = l[i - 1], l[i]
      i = i + 2
   print("".join(l))

if __name__ == '__main__':
   main()
