import sys
import random
def lotto(m):
   l = []
   while len(l) != 6:
      r = random.randint(1,47)
      if r not in l:
         l.append(r)
   matches = 0
   for ln in l:
      if str(ln) in m:
         matches = matches + 1
   return matches

def main():
   nums = []
   nums.append(sys.argv[1])
   nums.append(sys.argv[2])
   nums.append(sys.argv[3])
   nums.append(sys.argv[4])
   nums.append(sys.argv[5])
   nums.append(sys.argv[6])
   m3 = 0
   m4 = 0
   m5 = 0
   m6 = 0
   i = 0
   while i < 5000000:
      match = lotto(nums)
      if match == 3:
         m3 = m3 + 1
      elif match == 4:
         m4 = m4 + 1
      elif match == 5:
         m5 = m5 + 1
      elif match == 6:
         m6 = m6 + 1
         print(i)
      i = i + 1
   wid = len(str(m3))
   print("Match 3's : " + "{:>{:d}s}".format(str(m3), wid), "(" + str(i // m3), "to 1)")
   print("Match 4's : " + "{:>{:d}s}".format(str(m4), wid), "(" + str(i // m4), "to 1)")
   print("Match 5's : " + "{:>{:d}s}".format(str(m5), wid), "(" + str(i // m5), "to 1)")
   if 0 < m6:
      print("Match 6's : " +  "{:>{:d}s}".format(str(m6), wid), "(" +str(i // m6), "to 1)")
   else:
      print("Match 6's : " + "{:>{:d}s}".format("0", wid), "(? to 1)")

if __name__ == '__main__':
   main()
