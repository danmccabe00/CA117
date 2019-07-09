import sys

def big(l):
   i = 0
   while i < len(l) - 1:
      if l[i + 1] < l[i]:
         l.insert(i + 1, "-")
      i = i + 1
   return "".join(l)

def main():
   for lines in sys.stdin:
      ls = []
      for letters in lines.strip():
         ls.append(letters)
      extras = big(ls)
      print(max(extras.split("-"), key=len))

if __name__ == '__main__':
   main()
