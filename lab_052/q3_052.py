def build_dictionary(t):
   d = {}
   with open(t, "r") as f:
      line = f.readlines()
   for lines in line:
      an, val = lines.strip().split()
      d[an] = int(val)
   return d

def extract_range(d, low, high):
   b = {}
   for c in d:
      if low <= d[c] and d[c] <= high:
         b[c] = d[c]
   return b
