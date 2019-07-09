import sys

def sorter(t):
   return t[1]

def main():
   d = {}
   for lines in sys.stdin:
      l = lines.strip().split()
      score = int(l[-1]) + int(l[-2]) + int(l[-3])
      l.pop(-1)
      l.pop(-1)
      l.pop(-1)
      name = " ".join(l)
      d[name] = score
   for (k, v) in sorted(d.items(), key=sorter):
      max_v_width = len(str(max(d.values())))
      max_k_width = len(max(d.keys(), key=len))
      print('{:>{}s}: {:{}d}'.format(k, max_k_width, v, max_v_width))

if __name__ == '__main__':
   main()
