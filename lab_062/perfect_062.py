import sys

def sumFac(n):
   h = int(n ** (1 / 2))
   l = []
   i = 1
   while i <= h:
      if n % i == 0:
         m = n // i
         l.append(m)
         l.append(i)
      i = i + 1
   g = sum((l)[1:])
   if h ** 2 == n:
      return g + h
   else:
      return g


def isPerfect(n, m):
   #if m == 1:
      #return False
   if n == m:
      return True
   return False

def main():
   for lines in sys.stdin:
      #print((sumFac(int(lines.strip()))))
      print(isPerfect(sumFac(int(lines.strip())), int(lines.strip())))

if __name__ == '__main__':
   main()
