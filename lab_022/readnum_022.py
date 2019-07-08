import sys

a = []

def main():
   i = 0
   for lines in sys.stdin:
      a.append(lines.strip())
   while not a[i].isdigit():
      print(a[i], "is not a number")
      i = i + 1
   print("Thank you for", a[i])

if __name__ == '__main__':
   main()
