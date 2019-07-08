#!/isr/bin/env python

import sys

a = []
d = []

def vowels(l):
   b = []
   for w in l:
      if "a" in w and "e" in w and "i" in w and "o" in w and "u" in w:
         b.append(w)
   t = sorted(b, key=len)
   return t[0].strip()

def es(s):
   t = 0
   for w in s:
      if t < w.lower().count("e"):
         t = w.lower().count("e")
   return "{}".format([n.strip() for n in a if n.count("e") == t])


def main():
   for words in sys.stdin:
      a.append(words)
   print("Words containing 17 letters: " + "{}".format([n.strip() for n in a if len(n) == 18]))
   print("Words containing 18+ letters: " + "{}".format([n.strip() for n in a if 18 < len(n)]))
   print("Shortest word containing all vowels: " + vowels(a))
   print("Words with 4 a's: " + "{}".format([n.strip() for n in a if n.lower().count("a") == 4]))
   print("Words with 2+ q's: " + "{}".format([n.strip() for n in a if n.lower().count("q") > 1]))
   print("Words containing cie: " + "{}".format([n.strip() for n in a if "cie" in n]))
   print("Anagrams of angle: " + "{}".format([n.strip() for n in a if "a" in n.lower() and "n" in n.lower() and "g" in n.lower() and "l" in n.lower() and "e" in n.lower() and len(n) == 6 and "angle" not in n]))
   print("Words ending in iary: " + "{}".format(len([n.strip() for n in a if "iary" in n])))
   print("Words with most e's: " + str(es(a)))
if __name__ == '__main__':
   main()
