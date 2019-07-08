import sys
d = {"0": "zero",
     "1": "one",
     "2": "two",
     "3": "three",
     "4": "four",
     "5": "five",
     "6": "six",
     "7": "seven",
     "8": "eight",
     "9": "nine",
     "10": "ten",
     " ": " "}
b = {}
def main():
   b = {}
   with open(sys.argv[1]) as f:
      for line in f:
         eng, irish = line.strip().split()
         b[eng] = irish
   for lines in sys.stdin:
      a = ""
      n = lines.strip().split()
      for m in n:
         a = a + (b[d[m]]) + " "
      print(a[:-1])

if __name__ == '__main__':
   main()
