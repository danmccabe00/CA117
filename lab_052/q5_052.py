import sys

def sorter(t):
   return int(t[2])

def main():
   skip = []
   accept = []
   for lines in sys.stdin:
      tot = 0
      name, scores = lines.strip().split(":")
      a = scores.split(",")
      try:
         for nums in a:
            tot = tot + int(nums)
         p = name, ":", str(tot)
         accept.append(p)
      except:
         skip.append(name)
   accepted = sorted(accept, key=sorter, reverse=True)
   for k in accepted:
      print(" ".join(k))
   print("Skipped:")
   for y in skip:
      print(y)

if __name__ == '__main__':
   main()
