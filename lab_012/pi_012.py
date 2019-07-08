 #!/usr/bin/env python
 
import sys
from math import pi
def pie(r):
  m = str(r)
  n = "{:." + m + "f}"
  return(n.format(pi))
   

def main():
   print(pie(sys.argv[1]))

if __name__ == '__main__':
   main()
