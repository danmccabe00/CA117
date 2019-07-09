import sys

def roots1(a, b, c):
   if (b * b) - (4 * a * c) < 0:
      return None
   else:
      r1 = ((-b) + ((b * b) - (4 * a * c)) ** (1 / 2)) / (2 * a)
   return r1

def roots2(a, b, c):
   if (b * b) - (4 * a * c) < 0:
      return None
   else:
      r1 = ((-b) - ((b * b) - (4 * a * c)) ** (1 / 2)) / (2 * a)
   return r1


def main():
   for line in sys.stdin:
      try:
         a, b, c = line.strip().split()
         a, b, c = int(a), int(b), int(c)
         r1 = roots1(a, b, c)
         r2 = roots2(a, b, c)
         if r1 % 1 == 0 or r2 % 1 == 0:
            print("r1 = " + str((r1)) + ", r2 = " + str((r2)))
         elif r1 == 0 or r2 == 0:
            print(None)
         else:
            print(None)
      except:
         print(None)

if __name__ == '__main__':
   main()
