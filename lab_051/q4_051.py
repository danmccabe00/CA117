import sys

def main():
   l = []
   for lines in sys.stdin:
      l.append(int(lines.strip()))
   n = sum(l)
   r = "{:.1f}".format(n / len(l))
   print("Mean: " + str(r))
   m = len(l) / 2
   if m % 1 == 0:
      t = (sorted(l)[int(m)] + sorted(l)[int(m - 1)]) / 2
      print("Median: " + "{:.3s}".format(str(t)))
   else:
      p = sorted(l)[int(m - 0.5)]
      print("Median: " + str(p) + ".0")

if __name__ == '__main__':
   main()
