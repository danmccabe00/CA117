import sys

a = []
def main():
   errorl = []
   errors = 1
   for line in sys.stdin:
      l = []
      try:
         num, base = line.strip().split(" ", 1)
         num, base = int(num), int(base)
         try:
            while num != 0:
               l.append(num % base)
               num = (num // base)
            t = 0
            for a in l:
               t = t + (a ** 2)
            print(t)
            errors = errors + 1
         except:
            errors = errors + 1
            continue
      except:
         errorl.append(errors)
         errors = errors + 1
   if 0 < len(errorl):
      print("Failed to convert line(s): " + str(errorl)[1:-1] + " ")
if __name__ == '__main__':
   main()
