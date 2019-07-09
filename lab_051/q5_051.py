import sys

def times(l):
   f = 100000000000000000
   for c in l:
      mins, secs = c.split(":")
      t = (int(mins) * 60) + int(secs)
      if t < f:
         f = t
         best = c
   return best, f

def main():
   best = 100000000000
   for lines in sys.stdin:
      try:
         t = lines.strip().split()
         name = t[0]
         t.pop(0)
         time, secs = times(t)
         if int(secs) < best:
            best = int(secs)
            bestn = name, ":", time
      except:
         pass
   print(" ".join(bestn))
if __name__ == '__main__':
   main()
