#!/isr/bin/env python

import sys

a = []
def qnou(w):
   w = w.replace("qu", "--")
   return "q" in w

def main():
   for words in sys.stdin:
      if qnou(words.lower()):
         a.append(words.strip())
   print("Words with q but no u:", a)
if __name__ == '__main__':
   main()
