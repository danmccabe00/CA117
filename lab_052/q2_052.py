import sys

t = ["a", "e", "i", "o", "u"]
def main():
   for lines in sys.stdin:
      l = []
      for c in lines.lower():
         if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            l.append(c)
      if l == t:
         print(lines.strip())

if __name__ == '__main__':
   main()
