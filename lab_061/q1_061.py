import sys

def main():
   l = []
   for letters in sys.argv[1]:
      l.append(letters)
   i = 1
   while i < len(l):
      l[i - 1], l[i] = l[i], l[i - 1]
      i = i + 2
   print("".join(l))

if __name__ == '__main__':
   main()
